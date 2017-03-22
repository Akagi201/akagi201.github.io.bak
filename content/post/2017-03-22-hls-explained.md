+++
date = "2017-03-22T17:04:50+08:00"
title = "HLS 协议详解"
slug = "hls-explained"

+++

## HLS 概述

HLS 全称是 HTTP Live Streaming, 是一个由 Apple 公司实现的基于 HTTP 的媒体流传输协议. 他跟 DASH 协议的原理非常类似. 通过将整条流切割成一个小的可以通过 HTTP 下载的媒体文件.

由于传输层协议只需要标准的 HTTP 协议, HLS 可以方便的透过防火墙或者代理服务器, 而且可以很方便的利用 CDN 进行分发加速, 并且客户端实现起来也很方便.

HLS 目前广泛地应用于点播和直播领域.

在 HTML5 页面上使用 HLS 非常简单:

直接:

```
<video src="example.m3u8" controls></video>
```

或者:

```
<video controls>
    <source src="example.m3u8"></source>
</video>
```

下面, 我将会概括性地介绍 HLS 协议的方方面面(暂时不包括 AES 加密部分的内容), 配合 HLS 的 RFC 食用效果更佳.

## HLS 协议详解

![hls_arch](http://akagi201.qiniudn.com/hls_arch.png)

上面是 HLS 整体架构图, 可以看出, 总共有三个部分: Server, CDN, Client.

其实, HLS 协议的主要内容是关于 M3U8 这个文本协议的, 其实生成与解析都非常简单. 为了更加直接地说明这一点, 我下面举两个简单的例子:

简单的 Media Playlist:

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:8
#EXT-X-MEDIA-SEQUENCE:2680

#EXTINF:7.975,
https://priv.example.com/fileSequence2680.ts
#EXTINF:7.941,
https://priv.example.com/fileSequence2681.ts
#EXTINF:7.975,
https://priv.example.com/fileSequence2682.ts
```

包含多种比特率的 Master Playlist:

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1280000
http://example.com/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000
http://example.com/mid.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=7680000
http://example.com/hi.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=65000,CODECS="mp4a.40.5"
http://example.com/audio-only.m3u8
```

* HLS 通过 URI(RFC3986) 指向的一个 Playlist 来表示一个媒体流.
* 一个 Playlist 可以是一个 Media Playlist 或者 Master Playlist, 使用 UTF-8 编码的文本文件, 包含一些 URI 跟描述性的 tags.
* 一个 Media Playlist 包含一个 Media Segments 列表,当顺序播放时, 能播放整个完整的流. 
* 要想播放这个 Playlist, 客户端需要首先下载他, 然后播放里面的每一个 Media Segment.
* 更加复杂的情况是, Playlist 是一个 Master Playlist, 包含一个 Variant Stream 集合, 通常每个 Variant Stream 里面是同一个流的多个不同版本(如: 分辨率, 码率不同).

### HLS Media Segments

* 每一个 Media Segment 通过一个 URI 指定, 可能包含一个 byte range.
* 每一个 Media Segment 的 duration 通过 `EXTINF` tag 指定.
* 每一个 Media Segment 有一个唯一的整数 Media Segment Number.
* 有些媒体格式需要一个 format-specific sequence 来初始化一个 parser, 在 Media Segment 被 parse 之前. 这个字段叫做 Media Initialization Section, 通过 `EXT-X-MAP` tag 来指定.

#### 支持的 Media Segment 格式

##### MPEG-2 Transport Streams

* 即最常见的 TS 文件.
* RFC: ISO_13818.
* Media Initialization Section: PAT(Program Association Table) 跟 PMT(Program Map Table).
* 每个 TS segment 必须值含一个 MPEG-2 Program.
* 每一个 TS segment 包含一个 PAT 和 PMT, 最好在 segment 的开始处, 或者通过一个 `EXT-X-MAP` tag 来指定.

##### Fragmented MPEG-4

* 即常提到的 fMP4.
* RFC: ISOBMFF.
* Media Initialization Section: `ftyp` box(包含一个高于 `ios6` 的 brand), `ftyp` box 必须紧跟在 `moov` box 之后. `moov` box 必须包含一个 `trak` box(对于每个 fMP4 segment 里面的 `traf` box, 包含匹配的 `track_ID`). 每个 `trak` box 应该包含一个 sample table, 但是他的 sample count 必须为 0. `mvhd` box 跟 `tkhd` 的 duration 必须为 0. `mvex` box 必须跟在上一个 `trak` box 后面.
* 不像普通的 MP4 文件包含一个 `moov` box(包含 sample tables) 和一个 `mdat` box(包含对应的 samples), 一个 fMP4 包含一个 `moof` box (包含 sample table 的子集), 和一个 `mdat` box(包含对应的 samples).
* 在每一个 fMP4 segment 里面, 每一个 `traf` box 必须包含一个 `tfdt` box, fMP4 segment 必须使用 movie-fragment relative addressing. fMP4 segments 绝对不能使用外部的 data references.
* 每一个 fMP4 segment 必须有一个 `EXT-X-MAP` tag.

##### Packed Audio

* 一个 Packed Audio Segment 包含编码的 audio samples 和 ID3 tags. 简单的打包到一起, 包含最小的 framing, 并且没有 per-sample timestamp.
* 支持的 Packed Audio: AAC with ADTS
   framing [ISO_13818_7], MP3 [ISO_13818_3], AC-3 [AC_3], Enhanced
   AC-3 [AC_3].
* 一个 Packed Audio Segment 没有 Media Initialization Section.
* 每一个 Packed Audio Segment 必须在他的第一个 sample 指定 timestamp 通过一个 ID3 PRIV tag.
* ID3 PRIV owner identifier 必须是 `com.apple.streaming.transportStreamTimestamp`.
* ID3 payload 必须是一个 33-bit MPEG-2 Program Elementary Stream timestamp 的大端 eight-octet number, 高 31 为设置为 0.

##### WebVTT

* 一个 WebVTT Segment 是一个 WebVTT 文件的一个 section, WebVTT Segment 包含 subtitles.
* Media Initialization Section: WebVTT header.
* 每一个 WebVTT Segment 必须有以一个 WebVTT header 开始, 或者有一个 `EXT-X-MAP` tag 来指定.
* 每一个 WebVTT header 应该有一个 `X-TIMESTAMP-MAP` 来保证音视频同步.

### HLS Playlists

* Playlist 文件的格式是起源于 M3U, 并且继承两个 tag: `EXTM3U` 和 `EXTINF`
* 下面的 tags 通过 `BNF-style` 语法来指定.
* 一个 Playlist 文件必须通过 URI(.m3u8 或 m3u) 或者 HTTP Content-Type 来识别(application/vnd.apple.mpegurl 或 audio/mpegurl).
* 换行符可以用 `\n` 或者 `\r\n`.
* 以 `#` 开头的是 tag 或者注释, 以 `#EXT` 开头的是 tag, 其余的为注释, 在解析时应该忽略.
* Playlist 里面的 URI 可以用绝对地址或者相对地址, 如果使用相对地址, 那么是相对于 Playlist 文件的地址.

#### Attribute Lists
* 有的 tags 的值是 Attribute Lists.
* 一个 Attribute List 是一个用逗号分隔的 attribute/value 对列表.
* 格式为: `AttributeName=AttributeValue`.

#### Basic Tags

Basic Tags 可以用在 Media Playlist 和 Master Playlist 里面.

* `EXTM3U`: 必须在文件的第一行, 标识是一个 Extended M3U Playlist 文件.
* `EXT-X-VERSION`: 表示 Playlist 兼容的版本.

#### Media Segment Tags

每一个 Media Segment 通过一系列的 Media Segment tags 跟一个 URI 来指定. 有的 Media Segment tags 只应用与下一个 segment, 有的则是应用所有下面的 segments. 一个 Media Segment tag 只能出现在 Media Playlist 里面.

* `EXTINF`: 用于指定 Media Segment 的 duration
* `EXT-X-BYTERANGE`: 用于指定 URI 的 `sub-range`
* `EXT-X-DISCONTINUITY`: 表示不连续.
* `EXT-X-KEY`: 表示 Media Segment 已加密, 该值用于解密.
* `EXT-X-MAP`: 用于指定 Media Initialization Section.
* `EXT-X-PROGRAM-DATE-TIME`: 和 Media Segment 的第一个 sample 一起来确定时间戳.
* `EXT-X-DATERANGE`: 将一个时间范围和一组属性键值对结合到一起.

#### Media Playlist Tags

Media Playlist tags 描述 Media Playlist 的全局参数. 同样地, Media Playlist tags 只能出现在 Media Playlist 里面.

* `EXT-X-TARGETDURATION`: 用于指定最大的 Media Segment duration.
* `EXT-X-MEDIA-SEQUENCE`: 用于指定第一个 Media Segment 的 Media Sequence Number.
* `EXT-X-DISCONTINUITY-SEQUENCE`: 用于不同 Variant Stream 之间同步.
* `EXT-X-ENDLIST`: 表示结束.
* `EXT-X-PLAYLIST-TYPE`: 可选, 指定整个 Playlist 的类型.
* `EXT-X-I-FRAMES-ONLY`: 表示每个 Media Segment 描述一个单一的 I-frame.

#### Master Playlist Tags

Master Playlist tags 定义 Variant Streams, Renditions 和 其他显示的全局参数. Master Playlist tags 只能出现在 Master Playlist 中.

* `EXT-X-MEDIA`: 用于关联同一个内容的多个 Media Playlist 的多种 renditions.
* `EXT-X-STREAM-INF`: 用于指定一个 Variant Stream.
* `EXT-X-I-FRAME-STREAM-INF`: 用于指定一个 Media Playlist 包含媒体的 I-frames.
* `EXT-X-SESSION-DATA`: 存放一些 session 数据.
* `EXT-X-SESSION-KEY`: 用于解密.

#### Media or Master Playlist Tags

这里的 tags 可以出现在 Media Playlist 或者 Master Playlist 中. 但是如果同时出现在同一个 Master Playlist 和 Media Playlist 中时, 必须为相同值.

* `EXT-X-INDEPENDENT-SEGMENTS`: 表示每个 Media Segment 可以独立解码.
* `EXT-X-START`: 标识一个优选的点来播放这个 Playlist.

### 服务器端与客户端逻辑

以下流程仅供参考, 其实不同的播放器客户端以及服务器端的拉取规则都有很多细节差异.

#### 服务器端逻辑
1. 将媒体源切片成 Media Segment, 应该优先从可以高效解码的时间点来进行切片(如: I-frame).
1. 为每一个 Media Segment 生成 URI.
1. Server 需要支持 "gzip" 方式压缩文本内容.
1. 创建一个 Media Playlist 索引文件, `EXT-X-VERSION` 不要高于他需要的版本, 来提供更好的兼容性.
1. Server 不能随便修改 Media Playlist, 除了 Append 文本到文件末尾, 按顺序移除 Media Segment URIs, 增长 `EXT-X-MEDIA-SEQUENCE` 和 `EXT-X-DISCONTINUITY-SEQUENCE`, 添加 `EXT-X-ENDLIST` 到文件尾.
1. 在最后添加 `EXT-X-ENDLIST` tag, 来减少 Client reload Playlist 的次数.
1. 注意点播与直播服务器不同的地方是, 直播的 m3u8 文件会不断更新, 而点播的 m3u8 文件是不会变的, 只需要客户端在开始时请求一次即可.

#### 客户端逻辑
1. 客户端通过 URI 获取 Playlist. 如果是 Master Playlist, 客户端可以选择一个 Variant Stream 来播放.
1. 客户端检查 `EXT-X-VERSION` 版本是否满足.
1. 客户端应该忽略不可识别的 tags, 忽略不可识别的属性键值对.
1. 加载 Media Playlist file.
1. 播放 Media Playlist file.
1. 重加载 Media Playlist file.
1. 决定下一次要加载的 Media Segment.

## HLS 的优势
* 客户端支持简单, 只需要支持 HTTP 请求即可, HTTP 协议无状态, 只需要按顺序下载媒体片段即可.
* 使用 HTTP 协议网络兼容性好, HTTP 数据包也可以方便地通过防火墙或者代理服务器, CDN 支持良好.
* Apple 的全系列产品支持, 由于 HLS 是苹果提出的, 所以在 Apple 的全系列产品包括 iphone, ipad, safari 都不需要安装任何插件就可以原生支持播放 HLS, 现在, Android 也加入了对 HLS 的支持.
* 自带多码率自适应, Apple 在提出 HLS 时, 就已经考虑了码流自适应的问题.

## HLS 的劣势
* 相比 RTMP 这类长连接协议, 延时较高, 难以用到互动直播场景.
* 对于点播服务来说, 由于 TS 切片通常较小, 海量碎片在文件分发, 一致性缓存, 存储等方面都有较大挑战.

## 改进的 HLS 技术

由于客户端每次请求 TS 或 M3U8 有可能都是一个新的连接请求, 所以, 我们无法有效的标识客户端, 一旦出现问题, 基本无法有效的定位问题, 所以, 一般工业级的服务器都会对传统的 HLS 做一些改进.

这里主要介绍网宿的 Variant HLS 与又拍云的 HLS+.

### 网宿的 Variant HLS

首先, 我们可以下载一条网宿的 M3U8 文件:

`wget http://bililive.kksmg.com/hls/stvd6edb9a6_45b34047833af658bf4945a8/playlist.m3u8`

然后, 打开下载得到的 playlist 文件:

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=781000
http://bililive.kksmg.com/hls/stvd6edb9a6_45b34047833af658bf4945a8/playlist.m3u8?wsSession=0105cb4e8fe63bccab511a4a-149017212774715&wsIPSercert=b80d38c068c9e3634a7ebb2f2bbf9b89&wsMonitor=-1
```

可以看出这是一个 Master Playlist, 里面嵌套了一层 M3U8, 同时可以看出网宿采用 `wsSession` 来标识一条播放连接.

### 又拍云的 HLS+

#### Variant HLS

首先, 我们可以下载一条又拍云的 M3U8 文件:

`wget http://uplive.b0.upaiyun.com/live/loading.m3u8`

然后, 打开下载得到的 playlist 文件:

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-ALLOW-CACHE:YES
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-TARGETDURATION:1
#EXTINF:0.998, no desc
http://183.158.35.12:8080/uplive.b0.upaiyun.com/live/loading-0.ts?shp_uuid=e4989f34fcab282e21ef1fd2980284cb&shp_ts=1490172420851&shp_cid=17906&shp_pid=3370578&shp_sip0=127.0.0.1&shp_sip1=183.158.35.12&domain=uplive.b0.upaiyun.com&shp_seqno=0
```

可以看出又拍云的 HLS+ 也支持这种 Variant HLS 方式来标识一条 HLS 连接, 可以看出, 又拍云使用 uuid 来表示一条 HLS 连接.

#### HTTP 302

首先, 以 HTTP 302 方式来请求播放地址.

```
❯ curl -v http://uplive.b0.upaiyun.com/live/loading.m3u8\?shp_identify\=302 -o playlist
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 183.158.35.59...
* TCP_NODELAY set
* Connected to uplive.b0.upaiyun.com (183.158.35.59) port 80 (#0)
> GET /live/loading.m3u8?shp_identify=302 HTTP/1.1
> Host: uplive.b0.upaiyun.com
> User-Agent: curl/7.51.0
> Accept: */*
>
< HTTP/1.1 302 Found
< Server: marco/0.26
< Date: Wed, 22 Mar 2017 08:54:11 GMT
< Content-Type: text/plain; charset=utf-8
< Content-Length: 259
< Connection: keep-alive
< Access-Control-Allow-Methods: GET
< Access-Control-Allow-Origin: *
< Location: http://183.158.35.19:8080/uplive.b0.upaiyun.com/live/loading.m3u8?shp_uuid=2862b1b817a74cf719b1cd8f554616cd&shp_ts=1490172851450&shp_cid=59553&shp_pid=1730488&shp_sip0=127.0.0.1&shp_sip1=183.158.35.19&domain=uplive.b0.upaiyun.com&shp_identify=302
<
{ [259 bytes data]
* Curl_http_done: called premature == 0
100   259  100   259    0     0   4813      0 --:--:-- --:--:-- --:--:--  4886
* Connection #0 to host uplive.b0.upaiyun.com left intact
```

打开 playlist 内容:

```
Redirect to http://183.158.35.19:8080/uplive.b0.upaiyun.com/live/loading.m3u8?shp_uuid=2862b1b817a74cf719b1cd8f554616cd&shp_ts=1490172851450&shp_cid=59553&shp_pid=1730488&shp_sip0=127.0.0.1&shp_sip1=183.158.35.19&domain=uplive.b0.upaiyun.com&shp_identify=302
```

在跳转之后的地址存放真正的 playlist, 同时, 也能够将 uuid 加入到了连接上.

总地来说, 不管通过哪种方式, 最终我们都能通过一个唯一的 id 来标识一条流, 这样在排查问题时就可以根据这个 id 来定位播放过程中的问题.

## HLS 延时分析

```
HLS 理论延时 = 1 个切片的时长 + 0-1个 td (td 是 EXT-X-TARGETDURATION, 可简单理解为播放器取片的间隔时间) + 0-n 个启动切片(苹果官方建议是请求到 3 个片之后才开始播放) + 播放器最开始请求的片的网络延时(网络连接耗时)
```

为了追求低延时效果, 可以将切片切的更小, 取片间隔做的更小, 播放器未取到 3 个片就启动播放. 但是, 这些优化方式都会增加 HLS 不稳定和出现错误的风险.

## Demo

* [M3U8 golang library](https://godoc.org/github.com/osrtss/rtss/m3u8)
* [HLS downloader](https://github.com/osrtss/rtss/tree/master/m3u8/example/hlsdownloader): 读取一个 m3u8 URL, 下载为 TS 文件.

## Refs
* [HLS on wikipedia](https://en.wikipedia.org/wiki/HTTP_Live_Streaming)
* [Apple Developer](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/Introduction/Introduction.html)
* [流媒体协议—HLS](https://mp.weixin.qq.com/s?__biz=MzIyNDA1OTI2Nw==&mid=2666574360&idx=1&sn=ef1a484c04943c765f6fce5f2bddc83c&chksm=f310d8f4c46751e25c91a55817fac4a7f84476925c0bd88a4ca428c3e09c7f3c6357a8887f39&mpshare=1&scene=1&srcid=0322dFKxFXIYndfVLY1Lp289&key=41cc67db7e0a07a6eebe2fdab4a9db5ee1696265738d17dc51bb888e61e485c5be3ccc178acd6b5b185b05e28224c1ba3caa835627757343db3e940331d6afc3316ef7a03908fb727c630026c98a0f57&ascene=0&uin=MzczODI2ODU%3D&devicetype=iMac+MacBookPro11%2C3+OSX+OSX+10.12.3+build(16D32)&version=12020010&nettype=WIFI&fontScale=100&pass_ticket=weWVu89q646SDwy9dCFmksdsH21wbzfJgMDMyh4p88A%3D)