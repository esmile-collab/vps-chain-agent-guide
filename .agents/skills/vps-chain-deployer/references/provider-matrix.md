# 供应商核验矩阵（Agent 内部参考）

价格和库存会变。以下链接用于从官网开始，执行时必须重新打开并记录账单，不得把示例价格当承诺。

## VPS

| 供应商 | 官网入口 | 可作为的候选 | 现场核对 |
| --- | --- | --- | --- |
| BandwagonHost | https://bandwagonhost.com/cart.php | 日本/亚洲入口、不同网络系列 | 实际机房、线路名称、账期、续费、流量、IPv4 |
| DMIT Tokyo | https://www.dmit.io/pages/location/tokyo | 更看重亚洲路由质量的入口 | Tier 1/Premium 系列、东京库存、月付和续费、流量 |
| RackNerd | https://www.racknerd.com/ | 低成本美国或欧洲出口、实验 | 机房国家、促销库存、IPv4、到用户 ISP 的实测路由 |
| Hetzner Cloud | https://www.hetzner.com/cloud/ | 低价测试或自控出口 | 地区、计费单位、流量/带宽、IPv4、到用户 ISP 的实测路由 |

## 固定 ISP/住宅出口

| 供应商 | 官网入口 | 现场核对 |
| --- | --- | --- |
| ClipProxy | https://cliproxy.com/ | static、目标国家、SOCKS5、认证、并发、流量、UDP、到期和地区条款 |
| IPRoyal Static Residential | https://iproyal.com/pricing/static-residential-proxies/ | 独享/固定时长、SOCKS5/UDP、KYC、用途限制和续费 |
| Decodo ISP | https://decodo.com/proxies/isp-proxies/pricing | IP 数量、最低月费、税费、固定性、带宽和地区 |
| Bright Data ISP | https://brightdata.com/proxy-types/isp-proxies | 按 IP/流量计费、KYC、合同和可接受用途 |

供应商所说的“住宅”“ISP”“静态”可能对应不同产品。让用户买一个最小规格先测，不要一次预付大量 IP。通过 IPinfo 查看 ASN/组织类型，连续数日复查固定性。

## 付款前检查清单

1. URL 的域名与供应商名称一致，HTTPS 正常。
2. 记录一次性费用、续费费用、税费、退款窗口和自动续费。
3. 记录位置、IPv4/IPv6、流量、端口、并发和 UDP/TCP 能力。
4. 记录账号交付方式；密码由用户在供应商页面查看，Agent 不接收。
5. 对“保证解锁、永不封禁、100% 家宽”之类宣传要求书面条款或标记为未验证。
