#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


REQUIRED_NEEDS = (
    "monthly_budget",
    "first_payment_limit",
    "location_and_isp",
    "main_concern",
    "use_cases",
    "target_country_or_fixed_ip",
    "devices",
    "maintenance_tolerance",
)
VPS_EVIDENCE = (
    "checkout_price",
    "billing_cycle",
    "renewal_rule",
    "location_stock",
    "traffic_limit",
    "ipv4_included",
    "refund_rule",
    "acceptable_use",
    "route_test",
)
EXIT_EVIDENCE = (
    "checkout_price",
    "billing_cycle",
    "renewal_rule",
    "location_stock",
    "traffic_limit",
    "refund_rule",
    "acceptable_use",
    "static_allocation",
    "socks5_auth",
    "concurrency_limit",
    "udp_support",
    "route_test",
)
FRESHNESS_HOURS = {
    "checkout_price": 24,
    "billing_cycle": 24,
    "renewal_rule": 24,
    "location_stock": 24,
    "route_test": 72,
}
DEFAULT_FRESHNESS_HOURS = 168
SOURCE_KINDS = {"live_checkout", "official_page", "vendor_console", "network_test"}
REQUIRED_SOURCE_KINDS = {
    "checkout_price": {"live_checkout", "vendor_console"},
    "billing_cycle": {"live_checkout", "vendor_console"},
    "renewal_rule": {"live_checkout", "official_page", "vendor_console"},
    "location_stock": {"live_checkout", "vendor_console"},
    "route_test": {"network_test"},
}
VALUE_FIELDS = {
    "checkout_price": ("total_due", "currency", "tax_included"),
    "billing_cycle": ("months",),
    "renewal_rule": ("renewal_total", "currency", "auto_renewal"),
    "location_stock": ("location", "available"),
    "route_test": (
        "method",
        "tested_from",
        "target",
        "time_window",
        "latency_ms",
        "packet_loss_pct",
    ),
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def filled(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return value is not None


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def evidence_item(claim_id: str) -> dict[str, Any]:
    value: Any = ""
    if claim_id in VALUE_FIELDS:
        value = {field: None for field in VALUE_FIELDS[claim_id]}
    return {
        "claim_id": claim_id,
        "status": "unverified",
        "source_kind": "",
        "source": "",
        "checked_at": "",
        "evidence_excerpt": "",
        "value": value,
    }


def component(role: str) -> dict[str, Any]:
    claims = EXIT_EVIDENCE if role == "fixed_exit" else VPS_EVIDENCE
    return {
        "role": role,
        "provider": "",
        "product": "",
        "evidence": [evidence_item(claim) for claim in claims],
    }


def new_record(topology: str) -> dict[str, Any]:
    components = [component("entry_vps")]
    if topology == "chain":
        components.append(component("fixed_exit"))
    stamp = now_utc().replace(microsecond=0).isoformat()
    return {
        "schema_version": 1,
        "research_id": f"research-{stamp.replace(':', '').replace('+00:00', 'Z')}",
        "created_at": stamp,
        "user_needs": {
            key: [] if key in {"use_cases", "devices"} else ""
            for key in REQUIRED_NEEDS
        },
        "candidates": [{
            "id": "candidate-1",
            "name": "",
            "topology": topology,
            "cost_summary": "",
            "components": components,
            "unknowns": [],
        }],
        "decision": {"recommended_candidate_id": "", "reason": ""},
    }


def required_claims(role: Any) -> tuple[str, ...]:
    if not isinstance(role, str):
        return ()
    if role in {"entry_vps", "exit_vps", "backup_vps"}:
        return VPS_EVIDENCE
    if role == "fixed_exit":
        return EXIT_EVIDENCE
    return ()


def check_evidence(item: Any, path: str, claim: str, current: datetime) -> list[str]:
    if not isinstance(item, dict):
        return [f"{path}: 缺少证据 {claim}"]
    missing: list[str] = []
    if item.get("status") != "verified":
        missing.append(f"{path}.{claim}: 状态未验证")
    source_kind = item.get("source_kind")
    if not isinstance(source_kind, str) or source_kind not in SOURCE_KINDS:
        missing.append(f"{path}.{claim}: source_kind 无效")
    elif claim in REQUIRED_SOURCE_KINDS and source_kind not in REQUIRED_SOURCE_KINDS[claim]:
        allowed = " / ".join(sorted(REQUIRED_SOURCE_KINDS[claim]))
        missing.append(f"{path}.{claim}: source_kind 必须是 {allowed}")
    source = item.get("source")
    if not isinstance(source, str) or not source.startswith(("https://", "local-test:")):
        missing.append(f"{path}.{claim}: 缺少官网 URL 或 local-test 来源")
    checked_at = parse_time(item.get("checked_at"))
    if checked_at is None:
        missing.append(f"{path}.{claim}: checked_at 缺失或没有时区")
    else:
        max_age = timedelta(hours=FRESHNESS_HOURS.get(claim, DEFAULT_FRESHNESS_HOURS))
        if checked_at > current + timedelta(minutes=5):
            missing.append(f"{path}.{claim}: 核验时间在未来")
        elif current - checked_at > max_age:
            missing.append(f"{path}.{claim}: 证据已过期")
    if not filled(item.get("evidence_excerpt")):
        missing.append(f"{path}.{claim}: 缺少原文或测试摘录")
    value = item.get("value")
    if claim in VALUE_FIELDS:
        if not isinstance(value, dict):
            missing.append(f"{path}.{claim}: value 必须是对象")
        else:
            for field in VALUE_FIELDS[claim]:
                if not filled(value.get(field)):
                    missing.append(f"{path}.{claim}.value.{field}: 未填写")
        if isinstance(value, dict):
            if claim == "checkout_price" and not isinstance(value.get("total_due"), (int, float)):
                missing.append(f"{path}.{claim}.value.total_due: 必须是数字")
            if claim == "checkout_price" and not isinstance(value.get("tax_included"), bool):
                missing.append(f"{path}.{claim}.value.tax_included: 必须是 true 或 false")
            if claim == "billing_cycle" and not isinstance(value.get("months"), (int, float)):
                missing.append(f"{path}.{claim}.value.months: 必须是数字")
            if claim == "renewal_rule" and not isinstance(value.get("renewal_total"), (int, float)):
                missing.append(f"{path}.{claim}.value.renewal_total: 必须是数字")
            if claim == "renewal_rule" and not isinstance(value.get("auto_renewal"), bool):
                missing.append(f"{path}.{claim}.value.auto_renewal: 必须是 true 或 false")
            if claim == "location_stock" and not isinstance(value.get("available"), bool):
                missing.append(f"{path}.{claim}.value.available: 必须是 true 或 false")
            if claim == "route_test":
                for metric in ("latency_ms", "packet_loss_pct"):
                    if not isinstance(value.get(metric), (int, float)):
                        missing.append(f"{path}.{claim}.value.{metric}: 必须是数字")
    elif not filled(value):
        missing.append(f"{path}.{claim}: 缺少结构化结论")
    return missing


def evaluate(record: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    missing: list[str] = []
    if not isinstance(record, dict):
        return ["记录根节点必须是 JSON 对象"], []
    if record.get("schema_version") != 1:
        errors.append("schema_version 必须为 1")
    if not filled(record.get("research_id")):
        errors.append("research_id 缺失")
    if parse_time(record.get("created_at")) is None:
        errors.append("created_at 缺失、格式错误或没有时区")

    needs = record.get("user_needs")
    if not isinstance(needs, dict):
        errors.append("user_needs 必须是对象")
    else:
        for key in REQUIRED_NEEDS:
            if not filled(needs.get(key)):
                missing.append(f"user_needs.{key}: 用户需求未确认")

    candidates = record.get("candidates")
    if not isinstance(candidates, list) or not 1 <= len(candidates) <= 2:
        errors.append("candidates 必须包含 1 到 2 个候选")
        return errors, missing

    candidate_ids: set[str] = set()
    current = now_utc()
    for index, candidate in enumerate(candidates):
        base = f"candidates[{index}]"
        if not isinstance(candidate, dict):
            errors.append(f"{base} 必须是对象")
            continue
        candidate_id = candidate.get("id")
        if not isinstance(candidate_id, str) or not candidate_id.strip():
            errors.append(f"{base}.id 缺失或格式错误")
        elif candidate_id in candidate_ids:
            errors.append(f"{base}.id 缺失或重复")
        else:
            candidate_ids.add(candidate_id)
        for key in ("name", "topology", "cost_summary"):
            if not filled(candidate.get(key)):
                missing.append(f"{base}.{key}: 未填写")
        topology = candidate.get("topology")
        if not isinstance(topology, str) or topology not in {"direct", "chain", "dual_vps", "backup_entry"}:
            errors.append(f"{base}.topology 无效")

        components = candidate.get("components")
        if not isinstance(components, list) or not components:
            errors.append(f"{base}.components 必须是非空数组")
            continue
        roles = {
            part.get("role")
            for part in components
            if isinstance(part, dict) and isinstance(part.get("role"), str)
        }
        if "entry_vps" not in roles:
            missing.append(f"{base}: 缺少 entry_vps")
        if topology == "chain" and not ({"fixed_exit", "exit_vps"} & roles):
            missing.append(f"{base}: chain 缺少 fixed_exit 或 exit_vps")
        if topology == "dual_vps" and "exit_vps" not in roles:
            missing.append(f"{base}: dual_vps 缺少 exit_vps")
        if topology == "backup_entry" and "backup_vps" not in roles:
            missing.append(f"{base}: backup_entry 缺少 backup_vps")

        for part_index, part in enumerate(components):
            path = f"{base}.components[{part_index}]"
            if not isinstance(part, dict):
                errors.append(f"{path} 必须是对象")
                continue
            claims = required_claims(part.get("role"))
            if not claims:
                errors.append(f"{path}.role 无效")
                continue
            for key in ("provider", "product"):
                if not filled(part.get(key)):
                    missing.append(f"{path}.{key}: 未填写")
            evidence = part.get("evidence")
            if not isinstance(evidence, list):
                errors.append(f"{path}.evidence 必须是数组")
                continue
            by_claim: dict[str, Any] = {}
            for item in evidence:
                if isinstance(item, dict) and isinstance(item.get("claim_id"), str) and item.get("claim_id").strip():
                    claim_id = item["claim_id"]
                    if claim_id in by_claim:
                        errors.append(f"{path}.evidence: claim_id {claim_id} 重复")
                    by_claim[claim_id] = item
            for claim in claims:
                missing.extend(check_evidence(by_claim.get(claim), path, claim, current))

        unknowns = candidate.get("unknowns")
        if not isinstance(unknowns, list):
            errors.append(f"{base}.unknowns 必须是数组")
        else:
            for unknown_index, unknown in enumerate(unknowns):
                path = f"{base}.unknowns[{unknown_index}]"
                if not isinstance(unknown, dict):
                    errors.append(f"{path} 必须是对象")
                    continue
                if not filled(unknown.get("item")) or not filled(unknown.get("next_action")):
                    errors.append(f"{path} 必须填写 item 和 next_action")
                if unknown.get("blocking") is True:
                    missing.append(f"{path}: 仍有阻断项 {unknown.get('item', '')}")

    decision = record.get("decision")
    if not isinstance(decision, dict):
        errors.append("decision 必须是对象")
    else:
        recommended = decision.get("recommended_candidate_id")
        if not isinstance(recommended, str) or not recommended.strip():
            missing.append("decision.recommended_candidate_id: 尚未选择推荐候选")
        elif recommended not in candidate_ids:
            errors.append("decision.recommended_candidate_id 不在 candidates 中")
        if not filled(decision.get("reason")):
            missing.append("decision.reason: 未填写推荐依据")
    return errors, missing


def command_init(args: argparse.Namespace) -> int:
    output = Path(args.output).expanduser()
    if output.exists():
        print(f"ERROR: 文件已存在，未覆盖：{output}", file=sys.stderr)
        return 1
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(new_record(args.topology), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"已创建研究记录：{output}")
    return 0


def command_check(args: argparse.Namespace) -> int:
    path = Path(args.record).expanduser()
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: 找不到记录：{path}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: JSON 格式错误：{exc}", file=sys.stderr)
        return 1
    errors, missing = evaluate(record)
    if errors:
        print("记录格式错误：")
        for item in errors:
            print(f"- {item}")
        return 1
    if missing:
        print("UNVERIFIED：不得直接推荐。缺少或过期的证据：")
        for item in missing:
            print(f"- {item}")
        return 2
    print("READY：推荐门槛通过，可以按本记录给出明确推荐。")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="创建研究记录并检查供应商推荐硬门槛")
    commands = parser.add_subparsers(dest="command", required=True)
    init_parser = commands.add_parser("init", help="创建空白研究记录")
    init_parser.add_argument("--topology", choices=("direct", "chain"), required=True)
    init_parser.add_argument("--output", required=True)
    init_parser.set_defaults(handler=command_init)
    check_parser = commands.add_parser("check", help="检查记录能否形成明确推荐")
    check_parser.add_argument("record")
    check_parser.set_defaults(handler=command_check)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
