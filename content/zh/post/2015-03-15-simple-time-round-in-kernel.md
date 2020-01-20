+++
title = "简单的内核态时间片轮转程序"
date = "2015-03-15T10:45:08+08:00"
slug = "simple-time-round-in-kernel"

+++

## 实验环境
* 硬件: qemu(i386)(TODO: 由于我的gentoo没有装图形界面, 暂时在实验楼上做的)
* OS: linux-3.94 + [patch](https://raw.github.com/mengning/mykernel/master/mykernel_for_linux3.9.4sc.patch)
* 程序: <https://github.com/mengning/mykernel/tree/master/mykernel-1.1>
* repo: <https://github.com/Akagi201/learning-kernel/tree/master/kernel-inside/week2/mykernel>

## lab

### test1 环境测试
* 测试下环境, 仅仅是模拟了时钟中断, 一直都是一个进程在运行.
* `cd LinuxKernel/linux-3.9.4`
* `qemu -kernel arch/x86/boot/bzImage`

![mykernel-start](http://akagi201.qiniudn.com/mykernel-start.png)

### test2 运行时间片轮转程序
* 更新`mykernel`下的`myinterrupt.c`, `mymain.c`, `mypcb.h` 为: <https://github.com/Akagi201/learning-kernel/tree/master/kernel-inside/week2/mykernel/1.0> (复制不方便的话, 实验楼提供的ssh的方式连接系统)
* `make allnoconfig`
* `make`
* `qemu -kernel arch/x86/boot/bzImage`

## 分析

### 进程的启动
进程从`void __init my_start_kernel(void)`开始启动

嵌入式汇编代码, 初始化第0号进程

### 进程的切换
`schedule()`函数

未完待续.

## 备注

* 本文为刘博原创作品转载请注明出处.
* 《Linux内核分析》MOOC课程 <http://mooc.study.163.com/course/USTC-1000029000>