+++
title = "将OpenWrt变成完美的BSP"
date = "2014-07-03T12:26:26+08:00"
slug = "turn-openwrt-into-the-perfect-bsp"
githubIssuesID = 31

+++

BSP(Board Support Package)对于嵌入式开发者一定不陌生, 就是针对一种板子适配指定的操作系统(常见的是linux)所需要的bootloader, 板上外设的所有驱动, 还有内核, 通常还包括一个根文件系统(里面包含能确保板子能跑起来的基本的一些配置)和toolchain.

随着软件系统的发展, 越来越多的统一化环境配置的工具出现, 像vagrant, docker等, 这样, 将运行环境一起打包就不会出现过去那种, 在我的机器上能运行, 在你的机器上运行不了的情况了.

嵌入式开发也是一样, 每次面对一种新的SOC, 多要进行一些重复工作, 像裁剪系统, 裁剪busybox, 移植各种应用, 各种库等. 对于开发而言, 对于每种平台开发时, 都要有一些细小的差异. 而这些差异是可以统一起来的. 解决方案就是OpenWrt.

用OpenWrt作为BSP, 这使得用户和开发者可以快速熟悉不同的/新的硬件产品. 关于OpenWrt的详细内容, 在OpenWrt的官方文档有非常详细的介绍. <http://wiki.openwrt.org/doc/start>

那么公司如何用OpenWrt做自己的产品呢? 根据开源项目的特点需要进行一些修改.

## OpenWrt Buildroot的Makefile wrapper
* download tool: 下载指定版本的OpenWrt
* patchset: 对指定版本的OpenWrt进行打补丁, 确保稳定
* package feed: 自己软件包的 package feed.
* dl link directory: 将~/dl链接到openwrt/dl.

## 使用OpenWrt buildroot过程的技巧
* OpenWrt的buildroot编译系统, 包含fetching, patching, compiling, packaging的过程. 在fetching阶段会联网下载源码到dl目录, 所以, 一个好的方法是, 将dl目录保存在自己本地机器的一个固定位置, 然后软链接到openwrt/dl目录, 这样就不用每次下载重复的包了, 另外, 有时由于网络原因, 可以手动下载包放到这个目录.
* 
