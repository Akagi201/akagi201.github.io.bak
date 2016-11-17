+++
title = "Protothreads"
date = "2013-12-14T09:04:08+08:00"
slug = "protothreads"

+++

## Specs
* 没有专用的机器代码, 纯c实现.
* 不使用容易犯错的跳转指令.
* 占用极少内存.
* 在不在操作系统里用都可以提供blocking event-handlers(可阻塞的事件句柄??).
* 提供给事件触发系统(event-driven)线性代码执行(linear code execution).
* 提供顺序的控制流程(sequential flow of control)不需要使用复杂的状态机(state machine)或者完全的多线程(full multi-threading).
* Protothreads 是无优先级的, 因此, 一个上下文切换(context switch)只会发生在阻塞操作(blocking operations)上.
* Protothreads function as stackless, lightweight threads providing a blocking context cheaply using minimal memory per protothread (on the order of single bytes).
* Protothreads 是无栈的, 表示需要全局变量来保持变量用来跨上下文切换(across context switches).
* Protothread 的概念是被Adam Dunkels和Oliver Schmidt开发的.

## Adam Dunkels
* 看了一下他的wiki页面, 原来这个人还是个牛人, 在嵌入式领域写了不少东西.
* 博士, 瑞典的企业家和程序员, Thingsquare的创始人.
* IPSO Alliance的创始人, 推广对于小的设备(嵌入式和无线传感器)的IP网络通信. alliance's white paper的作者.
* 他的工作主要是关注网络技术和小的嵌入式设备和无线传感器的分布式通信.
* 作品有: uIP(micro-IP), lwIP, Protothreads, Contilki, uVNC, MiniWeb, phpstack, uBASIC.
* 书籍: <Interconnecting Smart Objects with IP - the Next Internet>.
* 

## Example
```C
#include "pt.h"
 
struct pt pt;
struct timer timer;
 
PT_THREAD(example(struct pt *pt))
{
  PT_BEGIN(pt);
 
  while(1) {
    if(initiate_io()) {
      timer_start(&timer);
      PT_WAIT_UNTIL(pt,
         io_completed() ||
         timer_expired(&timer));
      read_data();
    }
  }
  PT_END(pt);
}
```

## Refs
* <http://en.wikipedia.org/wiki/Protothreads>
* <http://dunkels.com/adam/pt/index.html>
* <http://en.wikipedia.org/wiki/Adam_Dunkels>
* <http://www.amazon.com/Interconnecting-Smart-Objects-IP-Internet/dp/0123751659>
* <http://hi.baidu.com/hyper99/item/bcf1dbc50af11247a8ba9422>