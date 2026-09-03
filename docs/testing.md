# 部署后的检测

按顺序测，能快速定位是哪一层出问题：客户端 → VLESS 入站 → VPS 服务 → 出口 SOCKS5 → 目标网站。

## 常用网站

| 网站 | 看什么 | 怎么判断 |
| --- | --- | --- |
| [IPinfo](https://ipinfo.io/) | IP、国家、ASN、组织类型、Hosting/Proxy 标记 | 国家和 ASN 要符合购买目标；“住宅”标签要结合供应商说明和多日复查 |
| [BrowserLeaks IP](https://browserleaks.com/ip) | 浏览器看到的 IP、IPv4/IPv6、组织信息 | 不应出现本地公网 IP；IPv6 若绕过代理，先关闭或正确纳入路由 |
| [BrowserLeaks DNS](https://browserleaks.com/dns) / [DNSLeakTest](https://www.dnsleaktest.com/) | DNS 请求由谁解析 | 全局代理时不应暴露家庭运营商 DNS；分流模式要按预期解释 |
| [BrowserLeaks WebRTC](https://browserleaks.com/webrtc) | WebRTC 可能暴露的地址 | 浏览器测试中不应出现不希望暴露的本地或真实公网地址 |
| [Speedtest](https://www.speedtest.net/) | 延迟、下载、上传 | 直连和链路用同一设备、相近时间、相近服务器比较；速度取决于最慢的一段 |
| [ping.pe](https://ping.pe/) | 多地 Ping、丢包、路由 | 看中位延迟和丢包趋势，不用单次尖峰下结论 |

服务器端可让 Agent 跑：`mtr -rwzc 100 目标地址`。目标地址由用户指定；不要扫描无关网段。

## 验收清单

1. VPS SSH 可登录，Xray 服务重启后自动恢复。
2. 只开 VLESS 时，出口 IP 是入口 VPS 的 IP/国家。
3. 加入 SOCKS5 后，出口 IP、国家和 ASN 变成购买的目标出口。
4. 连续多次检查结果一致，至少隔几个小时再复查一次固定性。
5. DNS、IPv6、WebRTC 没有泄露不希望暴露的地址。
6. 延迟、丢包、速度达到用户自己设定的最低线；项目不替用户臆造统一阈值。
7. 需要游戏、语音或视频会议时，单独测试 UDP/QUIC；SOCKS5 只支持 TCP 时要明确告知。
8. Windows 和 Apple 客户端分别测试，确认系统代理/TUN 的范围符合预期。

检测站点只能说明当前网络表现，无法保证某个平台长期接受该 IP。遇到登录或风控限制时遵守平台规则，不靠频繁换 IP 规避。
