+++
title = "保护你的隐私, 从PGP开始"
date = "2014-03-29T07:11:08+08:00"
slug = "protect-your-privacy-with-pgp"

+++

以前大学还在玩ubuntu的时候, 天天逛ubuntu的中文论坛, 看到这么个家伙, <http://adam8157.info/about>, 他的about页面一直放了一个`My PGP/GPG key ID: 2F39D84D`, 我一直不知道是干什么用的, 我还特意到知乎上问了一下, 不过貌似知乎对这么被认为是可google的问题没兴趣(对八卦和吐槽感兴趣?), 没得到满意答案, 今天有个空挡, 还是自己研究下.

PGP(OpenPGP)是一个历史悠久的电子加密和签章系统, 透过public key加密演算法, 保护个人电子资料, 不会在散布过程或存储媒体中被有心者窥视, 破坏或伪装. 不同于一般以CA(Certificate Authority, 认证机构)为基础的签章, 加密系统, PGP是分散式的系统, PGP没有中央的控制或信任机构, 因此不会被政府, 少数机构所控制,入侵. 在这个公权力无法被信任的年代, 我们正需要这样的系统, 保护我们的通讯安全.

## Web Of Trust

PGP是透过所谓的web of trust, 建构信任网. 也对于, 透过人际网路, 一对一的交换PGP key(public key), 安全的通讯管道, 建立在人和人之们的信任感上. 相对的, 以CA为基础的系统, 是透过少数集中的组织, 交换public key. 因此, CA容易受政府或少数机构的控制, 而破坏其安全性. 而web of trust则没这样的问题, 没有中央机构可以伪造你的PGP key. PGP的使用者, 透过web of trust确保所使用的 key, 不是政府或第三方所伪造的.

* Web Of Trust的运作: <http://www.pgpi.org/doc/pgpintro/#p20>

## 伪造Public Key

CA为基础的系统, Public Key的散布是透过CA对Public Key进行签名. CA会有一份公开的Public Key, 透过使用对应的secret key对某Public Key签名, 由CA保证其正确性. 而使用者, 透过验证通讯对方的Public Key是否有CA的正确签名, 确保使用正确的Public Key. 这样的系统, 建立在对CA的信任, 因此CA必需是公信的第三者. 然而, 事实上没有绝对公信的第三者, 政治力量随时可能入侵CA, 透过CA的Key, 伪造任何人的Public Key. 因此, 像CA这类中央式的系统, 容易受外力影向, 进行大规模隐私侵害, 无法保护通信的自由和隐密. 事实上, 中国某CA运作单位, 就被怀疑有这种[可能](http://blog.nutsfactory.net/2010/02/02/remove-cnnic-cert-on-linux/).

## PGP工具

PGP系统的实现, 有两项主要工具, PGP和GPG. PGP是原先的实现, 而GPG则是GNU实现的相容工具, 和PGP相容. 本文介绍GPG的使用.

## 产生PGP Key

GPG基本上会产生两对key, 一组用来sign(签章), 另一组用来encrypt(加密).  Encryption用途的key, 因为比较常被使用, 因此较容易受攻击. (透过分析加密的样本, 数量愈多, 愈可能分析出原本的key.) 因此, 一般建议定期更换加密用的 key. 然而, 更换key非常麻烦, 必需一一重新和拥有你的key的朋友交换. 因此, 签章用途的key通常是和加密用途的key分开的. 签章用途的key较少使用, 因此较不易被破解, 通常是永久使用. 在你更换新加密用途的key时, 能够使用签章用途的key, 为新的key签名. 因此, 你可以透过email或其它网路的方式散布你加密用途的新key. 收到新key的朋友, 就可以使用你签章用途的key, 验证你的新key.

产生新的PGP key的方法:

```
## 两种安装方法
#1. brew install gnupg # 命令行和linux完全一样
#2. https://gpgtools.org/ # GUI界面, 其实命令行就够了

akagi201@akrmbp ~ $ gpg --gen-key
gpg (GnuPG) 1.4.16; Copyright (C) 2013 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

gpg: directory `/Users/akagi201/.gnupg' created
gpg: new configuration file `/Users/akagi201/.gnupg/gpg.conf' created
gpg: WARNING: options in `/Users/akagi201/.gnupg/gpg.conf' are not yet active during this run
gpg: keyring `/Users/akagi201/.gnupg/secring.gpg' created
gpg: keyring `/Users/akagi201/.gnupg/pubring.gpg' created
Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 4
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048)
Requested keysize is 2048 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0)
Key does not expire at all
Is this correct? (y/N) y

You need a user ID to identify your key; the software constructs the user ID
from the Real Name, Comment and Email Address in this form:
    "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

Real name: Akagi201
Email address: akagi201@gmail.com
Comment: Bob Liu
You selected this USER-ID:
    "Akagi201 (Bob Liu) <akagi201@gmail.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
...+++++
..+++++
gpg: /Users/akagi201/.gnupg/trustdb.gpg: trustdb created
gpg: key BAD7F7A3 marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
pub   2048R/BAD7F7A3 2014-05-27
      Key fingerprint = E19A 2B9C B30F 8D0E 3F14  8C9F 7BAA 088C BAD7 F7A3
uid                  Akagi201 (Bob Liu) <akagi201@gmail.com>

Note that this key cannot be used for encryption.  You may want to use
the command "--edit-key" to generate a subkey for this purpose.
```

建议选(3)或者(4)(我选了4), 产生只用来签章的key, 并将有效时间设定为永远. 在产生签章用途的key之后, 该key会存在keyring里, 通常是home目录下的.gnupg 子目录, 你能用gpg列出目前存在的key.

```
akagi201@akrmbp ~ $ gpg --list-keys
/Users/akagi201/.gnupg/pubring.gpg
----------------------------------
pub   2048R/BAD7F7A3 2014-05-27
uid                  Akagi201 (Bob Liu) <akagi201@gmail.com>

akagi201@akrmbp ~ $ gpg --list-secret-keys
/Users/akagi201/.gnupg/secring.gpg
----------------------------------
sec   2048R/BAD7F7A3 2014-05-27
uid                  Akagi201 (Bob Liu) <akagi201@gmail.com>
```
这列出你有一把PGP的Public Key, 接着列出你有一把Secret Key. 这两把key的ID都是0xBAD7F7A3(第二栏, 斜线后), 代表他们是同一对key. Secret Key是使用者收藏(前面有sec字样), 不能让别人知道的部分, 用在签名用途. 而public key则是公开给别人知道(pub字样), 用来验证你的签名.

接着我们要产生加密用途的key.

```
akagi201@akrmbp ~ $ gpg --edit-key BAD7F7A3
gpg (GnuPG) 1.4.16; Copyright (C) 2013 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Secret key is available.

pub  2048R/BAD7F7A3  created: 2014-05-27  expires: never       usage: SC
                     trust: ultimate      validity: ultimate
[ultimate] (1). Akagi201 (Bob Liu) <akagi201@gmail.com>

gpg> addkey
Key is protected.

You need a passphrase to unlock the secret key for
user: "Akagi201 (Bob Liu) <akagi201@gmail.com>"
2048-bit RSA key, ID BAD7F7A3, created 2014-05-27

Please select what kind of key you want:
   (3) DSA (sign only)
   (4) RSA (sign only)
   (5) Elgamal (encrypt only)
   (6) RSA (encrypt only)
Your selection? 6
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048)
Requested keysize is 2048 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 2y
Key expires at Thu May 26 10:59:08 2016 CST
Is this correct? (y/N) y
Really create? (y/N) y
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
..+++++
.+++++

pub  2048R/BAD7F7A3  created: 2014-05-27  expires: never       usage: SC
                     trust: ultimate      validity: ultimate
sub  2048R/6E980A59  created: 2014-05-27  expires: 2016-05-26  usage: E
[ultimate] (1). Akagi201 (Bob Liu) <akagi201@gmail.com>

gpg> quit
Save changes? (y/N) y
```

请选择(5)或(6)(这里我选择了6), 产生专用来加密用的public key. 这里将有效时间设为两年(2y), 可依据需要设定. 完成之后, 会看到一把subkey(前面有sub字样), 这里得到的key ID为0x6E980A59. 0x6E980A59为0xBAD7F7A3的subkey. 0x6E980A59的有效期限为2年, 因此, 两年之后你必须生成一把新的key, 以取代这把.

```
kagi201@akrmbp ~ $ gpg --list-sigs
/Users/akagi201/.gnupg/pubring.gpg
----------------------------------
pub   2048R/BAD7F7A3 2014-05-27
uid                  Akagi201 (Bob Liu) <akagi201@gmail.com>
sig 3        BAD7F7A3 2014-05-27  Akagi201 (Bob Liu) <akagi201@gmail.com>
sub   2048R/6E980A59 2014-05-27 [expires: 2016-05-26]
sig          BAD7F7A3 2014-05-27  Akagi201 (Bob Liu) <akagi201@gmail.com>
```

这里可以看到, 0xBAD7F7A3和0x6E980A59这两把key都用0xBAD7F7A3这把key签章过(前面有sig字样). 也就是0xBAD7F7A3 有一个self-sign, 自已签自己.

```
akagi201@akrmbp ~ $ gpg --armor --export BAD7F7A3
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

mQENBFOD/ZQBCADQNTAV2KI+37d/Ep1ginwR2AoMTPe4AbhGVBr5LJsWbrW/y/Ap
Fyar6eAcT2OLAASpAyJNZpGxrG5QmKRjvcC/Bdx4mudWExs1o3aUwGIeCCUBVBdj
r0g2kZji/UbuaArRWVBotl/DIqvYswKM762FnQoOKTlMlj45U1dY1WS2ZP8KFhHV
5RWqJknY8p42QC5Tl09m7TCxkAz7ms+qU8Ya6Af4vLdSo8V7bpbATD2BQtPTpfZt
3z9rezvDRcsWK4O3Cmx5z+Q6HjQZV7Wbg2L3Q0yUzHktMM997WmRlT3zyUYXeAxG
wZSAGKcVd4gvHOLiRB5GyuYr8lIQH0GN/uCzABEBAAG0J0FrYWdpMjAxIChCb2Ig
TGl1KSA8YWthZ2kyMDFAZ21haWwuY29tPokBOAQTAQIAIgUCU4P9lAIbAwYLCQgH
AwIGFQgCCQoLBBYCAwECHgECF4AACgkQe6oIjLrX96OgqggAr21OZvGgqwo59G7H
9QGjwVD5OliJgAUuykEuzCv4ATKm+7Y/g/HgGUqIILKzknOPCe2VGTs+6RA98zWk
9nbdCUEu7oUZTBYq5h1uuPkm4FoJyyrwatSNChqJ4qav6jpZDqGnHwNeEwdY1WNG
uoC+MDM38u5KET6TnqYgmd5B0HWlUuiUx57uKE70vPRpziNDloeLzKdfD0fibKHN
ZFOgJJZkoPhr/yigqmQEfdrajTY4YGEy/2HYIULZYQs0paRe0SVw0UqbDZanOvlr
KOv6XFtH66DjY0pTgUWUXfGylzJAAtgQXQOFDXURC2oYG9DRkvA8q5gaZpqJT4f9
3Awk0bkBDQRTg/98AQgAwTKF9C/72yRmtTVaLziH93eKSc8jKOPt+Ncio5l+Bdhj
lJqJLzQWBB8uRa76wcTKMUpPMOPAMYqZjMekbVIrKFfNHh3pD+y90M/rDkhM2M4Z
gV6XtHnjqhQ4woqejM6k1ADKgndZNoau0TlJ7TagPM33Nay43vHo/BPcx6rs4Ssa
oSnv0sf4PBJeDfhjna+LVAQ18/rPBRijL/Xh6Bn2PWTrmF59g2mmdzV3WMOMsC+I
VkuXP20Vg4B0hFi6t9Hx/B5JL9t/xEEo2YKRyia8F4vtraSlhbMwVnfPfWuG5YSh
AsBa1ByLxCbNdELoLwU69ZDmgFH2x8JdUcm2vslwLwARAQABiQElBBgBAgAPBQJT
g/98AhsMBQkDwmcAAAoJEHuqCIy61/ejD9MH/A3vij2gjaLl3u1CAQB6n8DUSiyr
+bzEkoLHcJDYAM49oM3GPnkCSLJVM7EYmnlR6GOO4PwXlr2GjoxIer+MDCJ8hq98
n+H/2kgV8me/DDSoI1WUiIrcVLBcvylqZv3UWN4Vz+hP48iS/CEtPO6up/l3UAL3
YMWpi96+pnPodjMXL8JcIHlvx8Syxz1J0REI1J7uiGqzvJ9wu4ASYAHtJgi3qsvS
0FvAJcbdWMRNs51Pi0C1SYeztV7yRih8lTjI9ylUoncY5nKPtHrXjCNfpe0fClHx
JLz3WwlAX8gFyM3C+dl/622e7EvK9hO/spn8kS3lHD3q2V3t8GtSM4RzsY4=
=G9Ls
-----END PGP PUBLIC KEY BLOCK-----
```

透过上面的指令, 你能将你的public key export出来(导出), 印在纸上, 或存在U盘上, 或者是贴在网路上散布. 然而, 别人如何确定这把key是你的?

```
akagi201@akrmbp ~ $ gpg --fingerprint
/Users/akagi201/.gnupg/pubring.gpg
----------------------------------
pub   2048R/BAD7F7A3 2014-05-27
      Key fingerprint = E19A 2B9C B30F 8D0E 3F14  8C9F 7BAA 088C BAD7 F7A3
uid                  Akagi201 (Bob Liu) <akagi201@gmail.com>
sub   2048R/6E980A59 2014-05-27 [expires: 2016-05-26]
```

上面指令能列出你的public key的fingerprint(指纹)印出来, 这相当于public key浓缩之后的特征(digest). 因此, 其它使用者只需比对这组fingerprint是否和public key的相符, 就能确定这把key的正确性. 因此, 通常你会把fingerprint 印在纸上, 面对面交给对方. 必要时, 还会检查对方的身份证, 护照或其它身份证明文件.

## 交换key

在开始交换key之前, 建议先把你的public key上传到key server, 别人只需从key server上下载你的key. key server 是由第三方所维护的, 只负责key的散布, 而不负责签名, 因此不会有前面所述伪造的问题.

如下, 上传 0xBAD7F7A3这把key.(注意, 这里需要把shell的http代理关掉,否则上传失败) 上传完之后可以到<http://keys.gnupg.net/>查询.

```
akagi201@akrmbp ~ $ gpg --send-keys BAD7F7A3
gpg: sending key BAD7F7A3 to hkp server keys.gnupg.net
```

之后, 你只需告诉别人你的key id和fingerprint, 其它使用者就能下载和验证完整的public key.

```
akagi201@akrmbp ~ $ gpg --recv-keys BAD7F7A3
gpg: requesting key BAD7F7A3 from hkp server keys.gnupg.net
gpg: key BAD7F7A3: "Akagi201 (Bob Liu) <akagi201@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
akagi201@akrmbp ~ $ gpg --fingerprint
/Users/akagi201/.gnupg/pubring.gpg
----------------------------------
pub   2048R/BAD7F7A3 2014-05-27
      Key fingerprint = E19A 2B9C B30F 8D0E 3F14  8C9F 7BAA 088C BAD7 F7A3
uid                  Akagi201 (Bob Liu) <akagi201@gmail.com>
sub   2048R/6E980A59 2014-05-27 [expires: 2016-05-26]
```

例如, 本人的key ID是 0xBAD7F7A3. User ID为"Akagi201 (Bob Liu)"(前有uid字样). 你可以透过上面的指令下载我的 public key, 并验证fingerprint.

在下载和验证完成别人的public key之后, 若对方是你信任的人, 你可以为他的key签名. 当你为别人的key签名之后, 对方可以分布你的签名, 加强他的public key的可信度, 于是认识你的朋友, 可以依据你的签名, 决定是否相信该public key. 你也可以依据朋友的签名, 决定是否相信其它人的 public key.(下面的例子中我自己没法再给我自己签名了)

```
akagi201@akrmbp ~ $ gpg --sign-key BAD7F7A3

pub  2048R/BAD7F7A3  created: 2014-05-27  expires: never       usage: SC
                     trust: ultimate      validity: ultimate
sub  2048R/6E980A59  created: 2014-05-27  expires: 2016-05-26  usage: E
[ultimate] (1). Akagi201 (Bob Liu) <akagi201@gmail.com>

"Akagi201 (Bob Liu) <akagi201@gmail.com>" was already signed by key BAD7F7A3
Nothing to sign with key BAD7F7A3

Key not changed so no update needed.
```

上面的指令将使用你的secret key, 为 0xBAD7F7A3这把public key签章. 签完之后, 就可以看到0xBAD7F7A3这把key 多了一个签名. 你能将这个签名后的public key(再次)上传到key server, 或export成档案散布. 通常该public key 的原拥有者, 会希望取得你的签名.

```
akagi201@akrmbp ~ $ gpg --list-sigs
/Users/akagi201/.gnupg/pubring.gpg
----------------------------------
pub   2048R/BAD7F7A3 2014-05-27
uid                  Akagi201 (Bob Liu) <akagi201@gmail.com>
sig 3        BAD7F7A3 2014-05-27  Akagi201 (Bob Liu) <akagi201@gmail.com>
sub   2048R/6E980A59 2014-05-27 [expires: 2016-05-26]
sig          BAD7F7A3 2014-05-27  Akagi201 (Bob Liu) <akagi201@gmail.com>
```

## 加密

当你想要传送机密资料给其它人时, 可使用对方的public key为信件和资料加密. 只有对应的secret key, 才能解开该份信件或资料.

```
akagi201@akrmbp ~ $ gpg --armor --encrypt --output akmsg.asc akmsg.txt
You did not specify a user ID. (you may use "-r")

Current recipients:

Enter the user ID.  End with an empty line: Akagi201

Current recipients:
2048R/6E980A59 2014-05-27 "Akagi201 (Bob Liu) <akagi201@gmail.com>"

Enter the user ID.  End with an empty line:
akagi201@akrmbp ~ $ cat akmsg.asc
-----BEGIN PGP MESSAGE-----
Version: GnuPG v1

hQEMA4V0fiJumApZAQgAq5In+b2OiG7ruCfhbycUEUKgSTGrcSdErFuWHbWKpcSj
xItKaJX6s5FGGG01p4Q9h/kYzhOzwnxHmMDFszzcW9cxBSPXES5qpGJd5lO0PTCX
t7yma4geYmFG1zajkJzsnVyJl4NTvfnMgRcAKRqD5QZuo6vQNaURGsDtwcqY/iRt
6wD958HnBr3+OGkP6KCsjbhYsOrIaVnnfF0TEK0cxyCgu2743O8F9rwhwwTVBCMU
qHRXaHjRaGysflcnXlqHVRbHFYKTg+Mo2K2avricTKzu/bdV6J1jeCkqfXrbGKqD
aDxCmYZH1y7JmBNJJhYaWlth0b3Ir26+kO/RSOji2NJRAcJ1/bZK6uROY1LeuMps
G0zdH0ODNvV/sAe+9C23CqGFXrN/z4XdEHR1WyU3ZWUrPnEP4Z1hkQ2zy8ncy32I
92E6SyWit6R7KNbhHu8/A7jt
=F1tG
-----END PGP MESSAGE-----
akagi201@akrmbp ~ $ cat akmsg.txt
This is secret
```

例如上面的指令, 使用0x6E980A59这把key(0xBAD7F7A3的subkey), 将akmsg.txt这份文件加密, 并存成akmsg.asc. 上面指令中, 只需输入对方的email address或者user ID(uid), 就会从你的keyring中, 找出对方用来加密的public key.

## 解密

在你收到加密的文件时, 只需使用下面指令就可以使用存在keyring里的secret key, 为文件解密.

```
akagi201@akrmbp ~ $ rm akmsg.txt
akagi201@akrmbp ~ $ gpg --decrypt --output akmsg.txt akmsg.asc

You need a passphrase to unlock the secret key for
user: "Akagi201 (Bob Liu) <akagi201@gmail.com>"
2048-bit RSA key, ID 6E980A59, created 2014-05-27 (main key ID BAD7F7A3)

gpg: encrypted with 2048-bit RSA key, ID 6E980A59, created 2014-05-27
      "Akagi201 (Bob Liu) <akagi201@gmail.com>"
akagi201@akrmbp ~ $ cat akmsg.txt
This is secret
```

## 提醒

虽然可能性不是那么高, 但你永远不知道哪一天会需要这样的科技, 以保障你的通讯安全. 若不从现在开始建立你的web of trust, 需要时, 可能为时已晚. 请妥善保管你的secret key, 别让任何人有机可趁. 保护自己, 也保护朋友.


## Refs
* <http://www.codemud.net/~thinker/GinGin_CGI.py/show_id_doc/478>
