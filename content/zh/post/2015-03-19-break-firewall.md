+++
title = "break GxFxW"
date = "2015-03-19T11:32:26+08:00"
slug = "break-firewall"

+++

## GxFxW工作方式
* GxFxW本身是一个人人都知道他的存在, 却从来不会被官方承认的机构.
* GxFxW封锁重点: 新闻, 社交, 政治, 色情, 文件共享类网站.
* DNS劫持和污染: DNS缓存投毒, 虚假IP劫持, 空包劫持, 轻松的扩展污染.
* 敏感词过滤.
* IP阻断.

## 网络工具
* ping, tcping(可测tcp端口) 测试网络是否连通
* traceroute 显示路由跳跃情况
* route (netstat -nr) 打印和修改本地路由表
* dig/nslookup 解析域名

## OpenWrt组件
* ipset
* iptables-mod-ipopt, kmod-ipt-ipopt
* ip
* iptables-mod-filter, kmod-ipt-filter
* iptables-mod-u32, kmod-ipt-u32
* ppp-mod-pptp
* openvpn-ssl
* dnsmasq-full
* bind-dig, bind-libs

## 技术原理
* IP命令, `opkg install ip` table概念, 把数据添加到table, 让table数据走VPN接口.
* 

## Refs
* freerouter_v2 <http://www.lifetyper.com/>
* <http://www.chinagfw.org/>
* <https://zh.greatfire.org/>