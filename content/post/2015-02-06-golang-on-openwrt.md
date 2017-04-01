+++
title = "Golang on OpenWrt"
date = "2015-02-06T01:51:08+08:00"
slug = "golang-on-openwrt"
githubIssuesID = 45

+++

## Repo
* <https://github.com/GeertJohan/openwrt-go>

## Steps
* `git clone https://github.com/GeertJohan/openwrt-go`
* `git checkout add-gccgo-and-libgo`
* `make menuconfig`

```
-> Advanced configuration options
-> Toolchain options
....
-> Select Build/Install gccgo
....
-> C library implementation
-> Use eglibc
```

* `make V=s`

## result
* firmware with eglibc: `bin/ar71xx-eglibc/openwrt-ar71xx-generic-carambola2-squashfs-sysupgrade.bin`
* add toolchain to PATH: `export PATH=/home/akagi201/openwrt-go/staging_dir/toolchain-mips_34kc_gcc-4.8-linaro_eglibc-2.19/bin:$PATH`
* add toolchain alias: `alias mips_gccgo='mips-openwrt-linux-gccgo -Wl,-R,/home/akagi201/openwrt-go/staging_dir/toolchain-mips_34kc_gcc-4.8.0_eglibc-2.19/lib/gcc/mips-openwrt-linux-gnu/4.8.3 -L /home/akagi201/openwrt-go/staging_dir/toolchain-mips_34kc_gcc-4.8.0_eglibc-2.19/lib'`

## test
* use libgo non-static.

```
package main
import "fmt"
func main() {
    fmt.Println("hello world")
}
```

* `mips_gccgo -Wall -o hello_static_libgo hello.go -static-libgo`

* Before stripped

```
akagi201@akgentoo ~/openwrt-go (add-gccgo-and-libgo*) $ file hello_static_libgo
hello_static_libgo: ELF 32-bit MSB executable, MIPS, MIPS32 rel2 version 1, dynamically linked (uses shared libs), for GNU/Linux 2.6.16, not stripped

akagi201@akgentoo ~/openwrt-go (add-gccgo-and-libgo*) $ ll hello_static_libgo
-rwxr-xr-x 1 akagi201 akagi201 2.6M Feb  6 01:47 hello_static_libgo
```

* After stripped

```
akagi201@akgentoo ~/openwrt-go (add-gccgo-and-libgo*) $ file hello_static_libgo
hello_static_libgo: ELF 32-bit MSB executable, MIPS, MIPS32 rel2 version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.16, stripped
akagi201@akgentoo ~/openwrt-go (add-gccgo-and-libgo*) $ ll hello_static_libgo
-rwxr-xr-x 1 akagi201 akagi201 1.2M Feb  6 02:02 hello_static_libgo
```

## Refs
* <https://github.com/GeertJohan/openwrt-go/issues/2>