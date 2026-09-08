#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / ".agents" / "skills" / "vps-chain-deployer"
SKILL_FILE = SKILL_DIR / "SKILL.md"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    parts = text.split("---\n", 2)
    if len(parts) != 3:
        fail("SKILL.md frontmatter is not closed")

    result: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"unsupported frontmatter line: {line}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def check_skill() -> None:
    if not SKILL_FILE.is_file():
        fail(f"missing {SKILL_FILE.relative_to(REPO_ROOT)}")

    text = SKILL_FILE.read_text(encoding="utf-8")
    metadata = parse_frontmatter(text)

    name = metadata.get("name", "")
    description = metadata.get("description", "")

    if name != SKILL_DIR.name:
        fail("skill name must match its directory")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("skill name must use lowercase letters, digits, and hyphens")
    if len(name) > 64:
        fail("skill name exceeds 64 characters")
    if not description or len(description) > 1024:
        fail("skill description must contain 1 to 1024 characters")
    if "<" in description or ">" in description:
        fail("skill description cannot contain angle brackets")

    openai_yaml = SKILL_DIR / "agents" / "openai.yaml"
    if not openai_yaml.is_file():
        fail("missing agents/openai.yaml")
    openai_text = openai_yaml.read_text(encoding="utf-8")
    if "$vps-chain-deployer" not in openai_text:
        fail("openai.yaml default prompt must mention $vps-chain-deployer")


def check_local_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    errors: list[str] = []

    for markdown_file in REPO_ROOT.rglob("*.md"):
        if ".git" in markdown_file.parts:
            continue
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_text = target.split("#", 1)[0]
            if not path_text:
                continue
            resolved = (markdown_file.parent / path_text).resolve()
            if not resolved.exists():
                errors.append(
                    f"{markdown_file.relative_to(REPO_ROOT)} -> {target}"
                )

    if errors:
        fail("broken local Markdown links:\n" + "\n".join(errors))


def check_research_gate() -> None:
    gate_path = SKILL_DIR / "scripts" / "research_gate.py"
    spec = importlib.util.spec_from_file_location("research_gate", gate_path)
    if spec is None or spec.loader is None:
        fail("cannot load research_gate.py")
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)

    record = gate.new_record("direct")
    for key in record["user_needs"]:
        record["user_needs"][key] = ["test"] if isinstance(record["user_needs"][key], list) else "test"
    candidate = record["candidates"][0]
    candidate["name"] = "test candidate"
    candidate["cost_summary"] = "test total and monthly equivalent"
    component = candidate["components"][0]
    component["provider"] = "test provider"
    component["product"] = "test product"
    checked_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    for item in component["evidence"]:
        claim = item["claim_id"]
        value = "test value"
        if claim in gate.VALUE_FIELDS:
            value = {field: "test" for field in gate.VALUE_FIELDS[claim]}
            for field in ("total_due", "months", "renewal_total", "latency_ms", "packet_loss_pct"):
                if field in value:
                    value[field] = 1
            for field in ("tax_included", "auto_renewal", "available"):
                if field in value:
                    value[field] = False
        source_kind = "official_page"
        if claim in {"checkout_price", "billing_cycle", "location_stock"}:
            source_kind = "live_checkout"
        if claim == "route_test":
            source_kind = "network_test"
        item.update({
            "status": "verified",
            "source_kind": source_kind,
            "source": "local-test:route.txt" if claim == "route_test" else "https://example.com/",
            "checked_at": checked_at,
            "evidence_excerpt": "test evidence",
            "value": value,
        })
    record["decision"] = {
        "recommended_candidate_id": "candidate-1",
        "reason": "test reason",
    }
    errors, missing = gate.evaluate(record)
    if errors or missing:
        fail(f"complete research record should pass: errors={errors}, missing={missing}")

    component["evidence"][2]["status"] = "unverified"
    _, missing = gate.evaluate(record)
    if not any("renewal_rule" in item for item in missing):
        fail("research gate must block an unverified renewal rule")


def main() -> None:
    check_skill()
    check_local_markdown_links()
    check_research_gate()
    print("Skill metadata, local Markdown links, and research gate are valid.")


if __name__ == "__main__":
    main()
