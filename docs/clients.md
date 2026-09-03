# 客户端配置

服务端默认生成一个 `VLESS + Reality` 节点。完整节点链接只在你的设备之间传递，不要粘贴到聊天、网盘、二维码网站或公共订阅。

## 选择客户端

| 设备 | 首选 | 备用 | 说明 |
| --- | --- | --- | --- |
| Windows | [v2rayN](https://github.com/2dust/v2rayN/releases) | [Hiddify](https://github.com/hiddify/hiddify-app/releases) | 从官方发布页下载，按 x64/arm64 选择；先普通代理，TUN 后开 |
| macOS | [v2rayN](https://github.com/2dust/v2rayN/releases) | [Hiddify](https://github.com/hiddify/hiddify-app/releases) | Apple Silicon 和 Intel 选不同文件；只导入本地节点 |
| Android | [v2rayNG](https://github.com/2dust/v2rayNG/releases) | [Hiddify](https://github.com/hiddify/hiddify-app/releases) | 授予 VPN 权限；先全局测试，再考虑按应用分流 |
| iPhone/iPad | [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118) | [Hiddify](https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532) | App Store 的地区、价格和兼容性由用户自己确认 |
| Linux | [v2rayN](https://github.com/2dust/v2rayN/releases) | [Hiddify](https://github.com/hiddify/hiddify-app/releases) | 先确认桌面环境和发行版支持 |

v2rayN 官方项目支持 Windows、Linux 和 macOS；v2rayNG 面向 Android；Hiddify 官方项目覆盖 Android、iOS、Windows、macOS 和 Linux，并声明支持 VLESS/Reality。具体版本对某种 Reality 参数的兼容性仍需在你的设备上验收。

## 电脑端导入

1. Agent 在本机生成或显示二维码，或把完整链接暂存到本机剪贴板。
2. 从上表的官方来源安装客户端。
3. 导入节点，名称写清入口和出口，例如 `Tokyo-direct` 或 `Tokyo-US`。
4. 先选择普通代理/系统代理，访问一个普通网站并检查出口 IP。
5. 只有某个应用不跟随系统代理时，才考虑 TUN；开启前让 Agent 说明会接管哪些流量。

## 手机端导入

1. 在电脑本地打开 Agent 生成的二维码，手机直接扫描电脑屏幕。不要把链接上传到二维码网站。
2. 在手机官方商店或客户端官方发布页安装应用。
3. 扫描或粘贴节点，允许系统创建 VPN 配置。
4. 连接后先测 IP 和 DNS，再分别用 Wi-Fi、移动数据测试。
5. 关闭连接，清除剪贴板，删除二维码图片和临时截图。

Android 使用 v2rayNG 时，首次启动可能需要授予 VPN 权限；iPhone/iPad 使用 Shadowrocket 或 Hiddify 时，系统也会弹出 VPN 配置授权。授权弹窗只在你确认客户端来源正确后接受。

## 客户端故障判断

- 导入失败：先更新到官方最新版本，再让 Agent 在本机重新生成链接；不要把链接发到聊天里排查。
- 能连接但 IP 没变：确认启用了正确的配置和系统代理，检查应用是否绕过系统代理。
- 浏览器能用、某个应用不能用：先记录该应用是否支持系统代理，再考虑 TUN。
- Wi-Fi 能用、移动数据不能用：分别检查手机 VPN 权限和运营商网络，不要立即重建节点。
- 手机和电脑同时失败：从 VPS 服务、账单、出口到期和端口状态开始排查。
