+++
title = "Make A Live USB For MacBook"
date = "2015-05-18T06:09:26+08:00"
slug = "make-a-live-usb-for-macbook"
githubIssuesID = 55

+++

## live usb/live cd 发行版的选择
* <http://livecdlist.com/>
* 最开始使用的live usb是ubuntu, 因为是我的入门linux发行版. 不过后来越来越不喜欢这个不稳定的发行版了. 接触的有Knoppix(默认桌面有3d特性, 基于debian), kali linux(backtrack的新版本, 基于debian, 还不错哦, 玩的人还蛮多的), System Rescue CD(基于Gentoo是他唯一的优点了吧, 官方太多文档与实际不对应的问题了)
* 本次的选择, 先试用下System Rescue CD(因为我的项目就是用gentoo来做的, 另外, 我个人所有的linux环境都是gentoo啊), 如果发现使用起来非常不方便, 就转kali linux.

## System Rescue CD
* 官方只支持x86(32bit与64bit合二为一了, 应该是gentoo的multilib版本), 不支持ARM, 在树莓派上让我怎么愉快的玩耍! 不过想想, 对于树莓派的live usb, 应该叫做live sd才对, 只要有个可用的sd卡即可了. 我毕竟只有一个U盘(SLC, 16G), ARM版的live usb属实用的地方不多.

## Tools
* Mac Linux USB Loader: <http://sevenbits.github.io/Mac-Linux-USB-Loader/>
* Enterprise: <https://sevenbits.github.io/Enterprise/>

## mac上boot分析

不了解boot过程就搞的话, 很容易把系统搞坏的.

### uefi
### boot camp

## Ref
* <http://docs.kali.org/installation/kali-linux-dual-boot-on-mac-hardware>
* <http://www.makeuseof.com/tag/how-to-boot-a-linux-live-usb-stick-on-your-mac/>
* <http://mithun.co/tips/usb-live-boot-kali-linux-on-mac/>