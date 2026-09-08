# 供应商来源注册表（Agent 内部参考）

本表只保存稳定入口和必查项目，不保存套餐价格、库存结论或长期线路评价。所有动态信息进入本次 [研究记录](research-and-decision-gates.md)。

第三方发现入口：[DigVPS 测评总表](https://digvps.com/review)。它只用于发现候选和查看历史测评状态。购买、价格、续费、库存、产品能力和条款必须回到供应商官网核验。

## VPS 来源

| 供应商 | 官方产品/结账入口 | 官方条款/状态/测试入口 | 必查项目 |
| --- | --- | --- | --- |
| BandwagonHost | [购物车](https://bandwagonhost.com/cart.php) | [服务条款](https://bandwagonhost.com/knowledgebase/6/tos---terms-of-service.html)、[知识库](https://bandwagonhost.com/knowledgebase.php) | 产品系列、机房库存、本次付款、账期、续费与自动扣款、流量、IPv4、退款、用途限制、到用户网络的线路测试 |
| DMIT | [Tokyo](https://www.dmit.io/pages/location/tokyo) | [服务条款](https://www.dmit.io/pages/tos)、[可接受用途](https://www.dmit.io/pages/aup) | 网络系列、机房库存、本次付款、账期、续费、流量、IPv4、退款、地区/KYC 限制、到用户网络的线路测试 |
| RackNerd | [官网](https://www.racknerd.com/) | [服务条款](https://www.racknerd.com/terms-of-service)、[Looking Glass](https://lg-ash.racknerd.com/) | 促销是否仍可结账、机房、本次付款、账期、续费、流量、IPv4、退款、用途限制、用户本地晚高峰测试 |
| Hetzner Cloud | [Cloud](https://www.hetzner.com/cloud/) | [服务条款](https://www.hetzner.com/legal/terms-and-conditions/)、[服务状态](https://status.hetzner.com/) | 地区库存、本次付款、计费单位、续费/销毁规则、流量、IPv4 附加费、退款、身份核验、到用户网络的线路测试 |

官网没有公开 Looking Glass 时，先找官方测试 IP/下载文件或向售前索取。仍无法从用户所在网络实测，就把 `route_test` 保持 `unverified`，不能直接推荐。

## 固定 ISP/住宅出口来源

| 供应商 | 官方产品入口 | 官方条款/帮助入口 | 必查项目 |
| --- | --- | --- | --- |
| ClipProxy | [官网](https://cliproxy.com/) | [FAQ](https://help.cliproxy.com/faq) | 产品是否长期静态、目标国家、独享性、SOCKS5 与认证、并发、流量、UDP、到期/续费、退款、KYC、用途和地区限制、从入口 VPS 的实测 |
| IPRoyal | [Static Residential](https://iproyal.com/pricing/static-residential-proxies/) | [服务条款](https://iproyal.com/terms-of-service/)、[订阅条款](https://iproyal.com/subscription-terms/) | 独享性、固定时长、本次付款、账期、续费、SOCKS5、UDP、并发、流量、退款、KYC、用途限制、从入口 VPS 的实测 |
| Decodo | [ISP 产品页](https://decodo.com/proxies/isp-proxies/pricing) | 从产品页页脚进入当前条款 | 最低购买量、本次付款、税费、续费、固定性、带宽、认证、并发、UDP、KYC、用途限制、从入口 VPS 的实测 |
| Bright Data | [ISP 产品页](https://brightdata.com/proxy-types/isp-proxies) | 从产品页页脚进入当前条款 | 最低购买量、按 IP/流量计费、本次付款、续费、KYC、合同、地区和用途限制、认证、并发、UDP、从入口 VPS 的实测 |

供应商使用的“住宅”“ISP”“静态”可能指向不同产品。先买最小规格；购买后核验 ASN/组织类型并连续复查固定性。宣传中的“保证解锁”“永不封禁”“100% 家宽”没有可验证条款时，写入阻断性未确认项。

## 所有候选的必查证据

1. 官网域名、具体产品和可购买库存。
2. 结账页本次实际付款、币种、税费和账期。
3. 续费金额、续费周期、是否自动续费、取消方式。
4. 地区、IPv4/IPv6、流量/FUP、端口、并发和 TCP/UDP 能力。
5. 退款窗口、换 IP/迁移规则、KYC、可接受用途和地区限制。
6. 从用户实际网络到入口的测试；链式方案再测入口到出口。
7. 来源 URL、含时区核验时间、短原文或打码测试摘录、仍未确认项。

任何一项缺失时，按 [即时研究与推荐门槛](research-and-decision-gates.md) 输出“未验证”。
