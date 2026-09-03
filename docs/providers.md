# VPS 和固定出口怎么选

核验日期：2026-09-03。价格只作当天购买页的参考，库存、税费、优惠和续费可能变化。付款前让 Agent 打开链接重新核对。

## VPS

| 供应商 | 购买入口 | 公开页面的价格参考 | 适合场景 | 注意点 |
| --- | --- | --- | --- | --- |
| [BandwagonHost](https://bandwagonhost.com/cart.php) | 官网购物车 | 不同产品常见约 50 美元/季起 | 亚洲线路和日本机房，想少折腾 | 不同线路差异很大；以结账页的实际机房和续费为准 |
| [DMIT Tokyo](https://www.dmit.io/pages/location/tokyo) | 东京产品页 | Tier 1 小规格约 6.90 美元/月起；Premium 小规格约 21.90 美元/月起 | 更看重亚洲到中国的路由质量 | 价格高于低价 VPS；页面提示价格和库存以实际为准 |
| [RackNerd](https://www.racknerd.com/) | 官网 | 官网常见起步约 2.24 美元/月 | 低成本美国出口或实验 | 当前官网机房列表以美国/欧洲为主；从你的网络测量后再买 |
| [Hetzner Cloud](https://www.hetzner.com/cloud/) | 官网云主机 | 共享云主机常见约 3.49 美元/月起，地区不同会变 | 低成本测试、自己掌控出口 | 没有日本入口；中国方向体验必须实测 |

给 Agent 的购买动作：只读页面 → 记录产品和账期 → 计算月均成本 → 让用户确认 → 用户自行付款 → Agent 再接管服务器。不要因为某个历史套餐便宜就直接复用。

## 固定美国出口 / ISP（家宽）

| 供应商 | 入口 | 公开页面的价格参考 | 适合场景 | 购买前必须核对 |
| --- | --- | --- | --- | --- |
| [ClipProxy](https://cliproxy.com/) | 官网；[FAQ](https://help.cliproxy.com/faq) | 核验时长期静态产品页面约 3 美元/IP/月起 | 用户已在使用的固定出口供应商 | 静态 IP、美国地区、SOCKS5、认证方式、流量/并发、到期和地区条款 |
| [IPRoyal Static Residential](https://iproyal.com/pricing/static-residential-proxies/) | 价格页 | 核验时 90 天档约 2.40 美元/IP | 需要少量固定住宅/ISP IP | 是否独享、IP 是否长期不变、SOCKS5/UDP、KYC 和可接受用途 |
| [Decodo ISP](https://decodo.com/proxies/isp-proxies/pricing) | 价格页 | 核验时 3 个 IP 约 9.99 美元/月，另加税费 | 需要多个静态 ISP IP | IP 数量、月付最低额、税费、固定性、带宽和地区 |
| [Bright Data ISP](https://brightdata.com/proxy-types/isp-proxies) | 产品页 | 核验时 10 个 IP 约 18 美元/月 | 预算较高、需要供应商合规和支持 | KYC、合同/用途限制、按 IP 或流量计费；个人低预算通常不划算 |

“住宅”是供应商产品名称，不代表每个 IP 都像普通家庭宽带。购买后用 IPinfo 看 ASN/组织类型，并连续数天复查 IP 是否保持不变。不要购买免费代理、来源不明的共享账号或要求绕过供应商限制的产品。

## 成本怎么估

- VPS 直连：约 3–35 美元/月，取决于地区和网络系列。
- 链式方案：在入口 VPS 之外，再加约 3–20 美元/月的一个固定出口；高端合规供应商可能更贵。
- 双 VPS：按两台实际账单相加，另加备份和续费成本。

最终价格以付款页为准，Agent 只负责解释和记录，付款由用户完成。
