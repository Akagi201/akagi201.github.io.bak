+++
title = "无线基础之无线网卡"
date = "2014-05-05T07:14:26+08:00"
slug = "wireless-device"

+++

今天利用一个上午的时间把gentoo装好了, 昨天因为网线的原因导致我这边网络一直超时, 郁闷死我了, 多亏我今天足智多谋发现了. 由于OpenWrt的代码仓库版本更新非常频繁, 所以开发分支里面的库和内核版本比一般的桌面linux发行版都要新. 有一个基本常识是host开发主机上面的库和编译工具版本要比源码使用的版本新, 否则就会出现一些奇怪的问题, 无法解决. 所以, 选择一个滚动升级的linux发行版用于开发是明智的选择(相信我, 不难的). 这样筛选后就只剩下Arch和Gentoo了, Arch比较不稳定(希望不被喷, Arch的wiki跟Gentoo一样丰富是好东西), 所以Gentoo是你最明智的选择.用Gentoo编译了一下openwrt, 比我之前用debian节省了至少一半的时间, 哈哈, 爽. BTW, 不要给Gentoo安装图形界面, 很废时间, 也会出现很多冲突, 那就需要你身边有个高手了(我还不是要靠低调之神Yokit的帮忙才解决一些问题).

在进入无线研究之前你需要一套趁手的装备, 这套装备包括硬件和软件, 当然这个也就是我们要做的东西, 其中必然涉及一些硬件和软件的选型. 本文重点介绍一下网卡芯片的选型与相关知识.

## 常见网卡接口

* [PCI](http://en.wikipedia.org/wiki/Peripheral_Component_Interconnect)
* [USB](http://en.wikipedia.org/wiki/USB)
* [PCMCIA](http://en.wikipedia.org/wiki/PC_card)
* [Mini PCI](http://en.wikipedia.org/wiki/Mini_PCI#Mini_PCI)
* [PCI Express Mini](http://en.wikipedia.org/wiki/PCI_Express_Mini_Card#PCI_Express_Mini_Card).

## 底层芯片组

无论使用哪种接口的网卡, 他们的核心都是"芯片组". 这采集关键所在, 我们要关注的电气性能也是针对芯片组的. 目前常见的WLAN芯片厂商有:

1. [Atheros(已被高通收购)](https://wikidevi.com/wiki/Atheros)
2. [Broadcom(博通)](http://zh-cn.broadcom.com/)
3. [Intel](http://www.intel.com/content/www/us/en/wireless-network/wireless-products.html)
4. [Ralink(已被联发科收购)](http://www.ralinktech.com/en/)
5. [Realtek](http://www.realtek.com.tw/)

## 驱动程序

由于芯片的性能跟驱动的支持是分不开的, 所以, 良好的驱动支持, 也是我们要重点考虑的一项参数.
linux内核当前无线网卡驱动架构说明:
![mac80211](http://akagi201.qiniudn.com/mac80211.bmp)

可以看到linux下的无线驱动程序经过了一段"发展期", 最终以"mac80211驱动框架"作为最终的"主树结构".
关于mac80211驱动框架的详细文档请查看: <http://wireless.kernel.org/en/developers/Documentation/mac80211>.
mac80211是一个无线驱动的框架, 它提供了大量的API, 规范, 在这个框架下编写驱动程序能和其他的驱动具有良好的共享性, 兼容性(类似与windows下的NDIS框架的作用).

一般来说, 各家芯片厂商都会提供配套的驱动程序, 并提供更新支持
1. Atheros(AR系列)

```
<http://www.qca.qualcomm.com/resources/driverdownloads/>
<http://wireless.kernel.org/en/users/Drivers/Atheros>
```

2. Broadcom(BCM系列)

```
<http://zh-cn.broadcom.com/support/802.11/linux_sta.php>
<http://wiki.centos.org/zh/HowTos/Laptops/Wireless/Broadcom>
```

3. Intel

```
<http://wireless.kernel.org/en/users/Drivers/iwlwifi>
```

4. Ralink(RT系类)

```
<http://www.mediatek.com/en/downloads/>
```

淘宝上卖的很多卡皇的内置芯片就是这种RT型号(所谓卡皇就是无良厂家违规的放大了无线发射功率, 大家还是慎重考虑, wifi近距离接触(贴着身体)还是有危害的, 通常半米到1米左右还是可以认为是安全的)

5. Realtek(RTL系列)

```
<http://www.realtek.com.tw/DOWNLOADS/downloadsView.aspx?Langid=1&PNid=14&PFid=7&Level=5&Conn=4&DownTypeID=3&GetDown=false>
```

需要注意的, 我们在选择驱动的时候需要关注一下当前驱动是否支持USB(因为现在大多数人包括我自己都是使用外置网卡进行实验的).

## 待续

上面我们提到过, 不同型号的网卡的*主要差别*在于内置的芯片组, 但是, 一个无线网卡的好坏除了和上面说的芯片组, 驱动有关外, 还和他自身的一些物理, 电气特性有关, 下一篇我们会进一步与大家交流.

## Refs
* <http://en.wikipedia.org/wiki/Wireless_network_interface_controller>
* <http://www.freebuf.com/articles/wireless/33524.html>
* <http://blog.csdn.net/sudochen/article/details/8889719>

## Signature
* Author: Akagi201(我的微信, 加我请注明: 真实姓名-公司/专长)
* Blog: http://akagi201.org
* AK创客空间qq群: 212106391 (加群暗号: ak)
* 请支持本微信公众号, 分享给你的朋友们: AKmaker