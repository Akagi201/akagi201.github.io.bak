+++
title = "一个简单的汇编程序分析"
date = "2015-03-01T12:38:08+08:00"
slug = "a-simple-assembly-program-analysis"
githubIssuesID = 48

+++

最近打算跟一下<linux内核分析>这门mooc课程. 刚完成了第一周的内容. mindmup内容开源如下:

<iframe src="https://atlas.mindmup.com/akagi201/learning_kernel/index.html" width="600" height="800"></iframe>

这里使用跟linux内核一样的AT&T汇编语法.

## AT&T 汇编语法注意事项
* 大小写: 指令语句使用小写字母.
* 操作符赋值方向: 第一个为源操作数, 第二个为目的操作数, 方向从左到右, 合乎自然(与C库相反)
* 前缀: 寄存器需要加前缀"%", 立即数需要加前缀"$".
* 间接寻址语法: 使用 "(", ")"
* 后缀: 大部分指令操作码的最后一个字母表示操作数大小, "b"表示byte, "w"表示word(2个字节), "l"表示long(4个字节).
* 注释: @用于一行代码后面添加注释内容, #是整行注释.

## 简单的C源程序

```
/*
 * @file main.c
 * @author Akagi201
 * @date 2015/03/01
 *
 * A simple code to learn how assembly code works.
 * build on linux x64: gcc -S -o main.s main.c -m32
 */

int g(int x) {
  return x + 3;
}

int f(int x) {
  return g(x);
}

int main (void) {
  return f(8) + 1;
}

```

## Linux x64平台汇编命令

![asm](http://akagi201.qiniudn.com/assembly.png)

* 我的编译环境是: 物理机是rmbp, 运行的virtualbox, guest OS是gentoo x64.
* 汇编命令: `gcc –S –o main.s main.c -m32`
* 将得到的main.s文件中以.开头的行删掉(用于辅助链接的).
* 生成的汇编代码中增加了部分注释说明了程序执行的过程.

```
g:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %eax # eax = 8
	addl	$3, %eax # eax = 8 + 3 = 11
	popl	%ebp
	ret

f:
	pushl	%ebp
	movl	%esp, %ebp # 每个函数前两句都是这个, 用于保存上一个堆栈的栈顶, 跟清空出一个新的堆栈
	subl	$4, %esp
	movl	8(%ebp), %eax # eax = 8
	movl	%eax, (%esp) # 把8放到栈顶
	call	g # 跳到g标号
	leave
	ret

main:
	pushl	%ebp # 将当前ebp的值压栈, 同时esp的值被修改(即减4)
	movl	%esp, %ebp # 将ebp指向esp
	subl	$4, %esp # 将esp向下移动一个位置
	movl	$8, (%esp) # 将立即数8赋值给esp指向的位置(即当前的栈顶)
	call	f # 等价于两条语句 pushl eip; movl f eip => 当前eip实际指向addl $1, %eax这条指令, 跳转到f标号处执行
	addl	$1, %eax # eax = 11 + 1 = 12
	leave
	ret # 最终ebp, esp回到main函数最初的栈的位置.

```

## 备注

* 本文为刘博原创作品转载请注明出处.
* 《Linux内核分析》MOOC课程<http://mooc.study.163.com/course/USTC-1000029000>