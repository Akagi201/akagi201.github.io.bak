+++
date = "2015-09-11T20:03:26+08:00"
title = "取代netcat的瑞士军刀socat"
slug = "socat-extended-netcat"
githubIssuesID = 57

+++

## desc
* netcat++
* Multipurpose relay (SOcket CAT)
* <http://www.dest-unreach.org/socat/>
* 曾经一直纠结netcat这么好用的测试用具怎么就好久不更新了呢, 原来是有更好的取代者.
* socat相比netcat功能更加强大, 同时也相对复杂了一些.

## 包含的工具
* `socat`: establishes two bidirectional byte streams and transfers data between them.
* `filan`: prints information about its active file descriptors to stdout.
* `procan`: prints information about process parameters to stdout

## 工作原理 - life cycle of a `socat` instance (4 phases)
1. init phase(初始化阶段), the command line options are parsed and logging is initialized. (解析命令行以及初始化日志系统.)
2. open phase(打开连接阶段), opens the first address and afterwards the second address. These steps are usually blocking; thus, especially for complex address types like socks, connection requests or authentication dialogs must be completed before the next step is started. (先打开第一个连接, 再打开第二个连接. 这个单步执行的. 如果第一个连接失败, 则会直接退出.)
3. transfer phase(数据转发阶段), socat watches both streams' read and write file descriptors via select() , and, when data is available on one side and can be written to the other side, socat reads it, performs newline character conversions if required, and writes the data to the write file descriptor of the other stream, then continues waiting for more data in both directions. (谁有数据就转发到另外一个连接上, read/write互换.)
4. closing phase(关闭阶段), one of the streams effectively reaches EOF. Socat transfers the EOF condition to the other stream, i.e. tries to shutdown only its write stream, giving it a chance to terminate gracefully. For a defined time socat continues to transfer data in the other direction, but then closes all remaining channels and terminates. (其中一个连接断开, 执行处理另外一个连接.)

## Options
* 命令行参数用来修改程序的行为. 他们与所谓的作为address specifications的一部分的address options无关.
* 详见: `socat -h`

## Address specifications
* 一个address specification通常包含一个address type关键字, 0或者更多必要的address parameters与keyword用':'分隔以及他们相互之间, 和0或者更多address options用','分隔.
* keyword指定address type(如: TCP4, OPEN, EXEC). 对于有些keywords有同义词('-'与STDIO, TCP与TCP4). 关键字是大小写敏感的. 对于一些特殊的address type, keyword可以被忽略: Address specifications以数字开头的被认为是FD address(raw file descriptor). 如果一个'/'被发现, 在第一个':'或者','前, GOPEN(generic file open)被认定.
* 0或者更多address options可以被给到每一个地址上. 他们在一些方式上影响地址. Options由一个option keyword组成或者一个`option keyword=value`组成. Option keywords是大小写不敏感的.

## Address Types
* `socat -h`

## Address Options
* `socat -h`

## Data Values


## Refs
* <http://www.dest-unreach.org/socat/doc/socat.html>
* <http://www.dest-unreach.org/socat/doc/README>
