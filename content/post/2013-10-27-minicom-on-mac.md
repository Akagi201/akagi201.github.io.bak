+++
title = "minicom on mac"
date = "2013-10-27T05:41:08+08:00"
slug = "minicom-on-mac"
githubIssuesID = 5

+++

## USB转串口驱动
* 我使用的芯片是FTDI的根据FTDI官网的说明,需要下载VCP(Virtual COM Port)驱动.下载了64位的2.2.18版本,ps这东西版本也挺旧的了,是2012/08/08发布的.
* 另外一种适配器基于Silicon Labs的CP2012芯片, Windows, Linux和 Mac下都有驱动<http://www.silabs.com/products/mcu/pages/usbtouartbridgevcpdrivers.aspx>
* ps: 另外一种常见得USB转串口驱动(Prolific PL2303):
在Prolific官网上面也有:(http://www.prolific.com.tw/US/ShowProduct.aspx?pcid=41&showlevel=0041-0041).
* 参考文献中还有其他的驱动,有需要的可以到参考文献中去查.
* 安装前先删除已有的USB转串口驱动(我跳过了)
* 安装好之后,打开一个Terminal, 输入 ls /dev/cu.*, 找到包含有usbserial或类似的东西.我的结果:

```
    $ ls /dev/cu.*                                                             
    /dev/cu.Bluetooth-Incoming-Port /dev/cu.usbserial-AD02COJ7
    /dev/cu.Bluetooth-Modem
```

* 注意:一个serial device会在/dev下面出现2次, 一个是tty.*,用来 calling into UNIX systems, 一个是cu.*, (Call-Up)用来从他们中 calling out(如: modems).我们想要从我们的Mac中call-out所以我们选用/dev/cu.*.
* TTY device与CU device的技术区别是: 
/dev/tty.*会wait(或者listen)for DCD(data-carrier-detect),如:某人在response之前calling in.
/dev/cu.*不会assert DCD, 所以他们将总是立刻connect(respond or succeed).

## Terminal emulation
* GUI apps: Zterm(收费, 支持VT100 emulation), goSerial(不支持 VT100), SecureCRT for Mac(收费)
* Terminal apps: screen, minicom(recommend,and I used)
* built-in: screen(screen /dev/cu.usbserial-AD02COJ7 115200, 退出:  type CTRL-A, then CTRL-\.)

## Minicom
* 支持VT100 emulation(which means it sorta kinda works with Meridian Mail (Function keys on a MacBook: fn + f-key))
* 先运行minicom -s来配置, 修改device name和流控信息, 然后 Save setup as dfl(default) and Exit.
* 每次运行minicom前都记得插入usb转串口.
* 在minicom中, 命令都是 Ctrl-A <key>
修改port settings: Ctrl-A P
Command Summary: Ctrl-A Z
Quit Minicom: Ctrl-A X

## screen
Mac自带的命令行工具, 可以用来连接USB虚拟串口, 使用方法:

```
screen /dev/cu.SLAB_USBtoUART 115200
```

这里的/dev/cu.SLAB_USBtoUART是虚拟串口的设备文件节点, 确保装好了适配器的驱动, 插入适配器应该就会找到它们了. 电脑通过/dev/cu.*设备文件来连接其他串口设备, 通过/dev/tty.* 接受来自其他设备的连接.

## Refs
* [在mac下使用串口方法](http://pbxbook.com/other/mac-tty.html)
* [FTDI官网](http://www.ftdichip.com)
* <http://h4x3rotab.github.io/blog/2014/01/31/os-xxia-de-usbzhuan-uart/>