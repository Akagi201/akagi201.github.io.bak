+++
date = "2016-10-31T16:21:50+08:00"
title = "直播协议 HTTP-FLV 详解"
slug = "http-flv-explained"
githubIssuesID = 67

+++

传统的直播协议要么使用 Adobe 的基于 TCP 的 RTMP 协议, 要么使用 Apple 的基于 HTTP 的 HLS 协议.

今天我要向大家介绍另外一种结合了 RTMP 的低延时, 以及可以复用现有 HTTP 分发资源的流式协议 HTTP-FLV.

## FLV

首先, 一定要先介绍一下 FLV 文件格式的细节.

### FLV adobe 官方标准

FLV 文件格式标准是写在 [F4V/FLV file format spec v10.1](http://download.macromedia.com/f4v/video_file_format_spec_v10_1.pdf) 的附录 E 里面的 FLV File Format.

### 单位说明

| 类型            	| 说明                                                               	|
|-----------------	|--------------------------------------------------------------------	|
| Unit data types 	|                                                                    	|
| SI8             	| Signed 8-bit integer                                               	|
| SI16            	| Signed 16-bit integer                                              	|
| SI24            	| Signed 24-bit integer                                              	|
| SI32            	| Signed 32-bit integer                                              	|
| SI64            	| Signed 32-bit integer                                              	|
| UI8             	| Unsigned 8-bit integer                                             	|
| UI16            	| Unsigned 16-bit integer                                            	|
| UI24            	| Unsigned 24-bit integer                                            	|
| UI32            	| Unsigned 32-bit integer                                            	|
| UI64            	| Unsigned 64-bit integer                                            	|
| xxx[]           	| Slice of type xxx                                                  	|
| xxx[n]          	| Array of type xxx                                                  	|
| STRING          	| Sequence of Unicode 8-bit characters (UTF-8), terminated with 0x00 	|

### FLV 文件头和文件体 (E.2, E.3)

从整个文件上看, FLV = FLV File Header + FLV File Body

| 字段               	| 类型   	| 说明                                                           	|
|--------------------	|--------	|----------------------------------------------------------------	|
| FLV File Header    	|        	|                                                                	|
| Signature          	| UI8[3] 	| 签名, 总是 'FLV' (0x464C56)                                    	|
| Version            	| UI8    	| 版本, 总是 0x01, 表示 FLV version 1                            	|
| TypeFlagsReserved  	| UB [5] 	| 全 0                                                           	|
| TypeFlagsAudio     	| UB[1]  	| 1 = 有音频                                                     	|
| TypeFlagsReserved  	| UB[1]  	| 全 0                                                           	|
| TypeFlagsVideo     	| UB[1]  	| 1 = 有视频                                                     	|
| DataOffset         	| UI32   	| 整个文件头长度, 对于FLV v1, 总是 9                             	|
| FLV File Body      	|        	|                                                                	|
| PreviousTagSize0   	| UI32   	| 总是 0                                                         	|
| Tag1               	| FLVTAG 	| 第一个 tag                                                     	|
| PreviousTagSize1   	| UI32   	| 前一个 tag 的大小, 包括他的 header, 即: 11 + 前一个 tag 的大小 	|
| Tag2               	| FLVTAG 	| 第二个 tag                                                     	|
| ...                	|        	|                                                                	|
| PreviousTagSizeN-1 	| UI32   	| 前一个 tag 大小                                                	|
| TagN               	| FLVTAG 	| 最后一个 tag                                                   	|
| PreviousTagSizeN   	| UI32   	| 最后一个 tag 大小, 包括他的 header                             	|

通常, FLV 的前 13 个字节(flv header + PreviousTagSize0)完全相同, 所以, 程序中会单独定义一个常量来指定.

### FLV Tag (E.4)

| 字段              	| 类型   	| 说明                                                   	|
|-------------------	|--------	|--------------------------------------------------------	|
| FLV Tag           	|        	|                                                        	|
| Reserved          	| UB[2]  	| 保留给FMS, 应为 0                                      	|
| Filter            	| UB[1]  	| 0 = unencrypted tags, 1 = encrypted tags               	|
| TagType           	| UB [5] 	| 类型, 0x08 = audio, 0x09 = video, 0x12 = script data   	|
| DataSize          	| UI24   	| message 长度, 从 StreamID 到 tag 结束(len(tag) - 11)   	|
| Timestamp         	| UI24   	| 相对于第一个 tag 的时间戳(unit: ms), 第一个 tag 总是 0 	|
| TimestampExtended 	| UI8    	| Timestamp 的高 8 位. 扩展 Timestamp 为 SI32 类型       	|
| StreamID          	| UI24   	| 总是 0, 至此为 11 bytes                                	|
| AudioTagHeader    	|        	| IF TagType == 0x08                                     	|
| VideoTagHeader    	|        	| IF TagType == 0x09                                     	|
| EncryptionHeader  	|        	| IF Filter == 1                                         	|
| FilterParams      	|        	| IF Filter == 1                                         	|
| Data              	|        	| AUDIODATA 或者 VIDEODATA 或者 SCRIPTDATA               	|

Timestamp 和 TimestampExtended 组成了这个 TAG 包数据的 PTS 信息, PTS = Timestamp | TimestampExtended << 24.

### AudioTag (E.4.2)

由于 AAC 编码的特殊性, 这里着重说明了 AAC 编码的 Tag 格式.

| 字段           	| 类型                          	| 说明                                                                                  	|
|----------------	|-------------------------------	|---------------------------------------------------------------------------------------	|
| Audio Tag      	|                               	|                                                                                       	|
| AudioTagHeader 	|                               	|                                                                                       	|
| SoundFormat    	| UB[4]                         	| 音频编码格式. 2 = MP3, 10 = AAC, 11 = Speex                                           	|
| SoundRate      	| UB[2]                         	| 采样率. 0 = 5.5 kHz, 1 = 11 kHz, 2 = 22 kHz, 3 = 44 kHz                               	|
| SoundSize      	| UB[1]                         	| 采样大小. 0 = 8-bit, 1 = 16-bit                                                       	|
| SoundType      	| UB[1]                         	| 音频声道数. 0 = Mono, 1 = Stereo                                                      	|
| AACPacketType  	| UI8                           	| 只有当 SoundFormat 为 10 时, 才有该字段. 0 = AAC sequence header, 1 = AAC raw         	|
| AACAUDIODATA   	|                               	|                                                                                       	|
| Data           	| AudioSpecificConfig           	| IF AACPacketType == 0, 包含着一些更加详细音频的信息                                   	|
| Data           	| Raw AAC frame data in UI8 [n] 	| IF AACPacketType == 1, audio payload, n = [AAC Raw data length] - ([has CRC] ? 9 : 7) 	|

AudioTagHeader 的第一个字节, 也就是接跟着 StreamID 的 1 个字节包含了音频类型, 采样率等的基本信息.

AudioTagHeader 之后跟着的就是 AUDIODATA 部分了. 但是, 这里有个特例, 如果音频格式(SoundFormat)是 AAC, AudioTagHeader 中会多出 1 个字节的数据 AACPacketType, 这个字段来表示 AACAUDIODATA 的类型: 0 = AAC sequence header, 1 = AAC raw.

AudioSpecificConfig 结构描述非常复杂, 在标准文档中是用伪代码描述的, 这里先假定要编码的音频格式, 做一下简化.

音频编码为: `AAC-LC`, 音频采样率为 44100.

| 字段                   	| 类型  	| 说明                                	|
|------------------------	|-------	|-------------------------------------	|
| AudioSpecificConfig    	|       	|                                     	|
| audioObjectType        	| UB[5] 	| 编码结构类型, AAC-LC 为 2           	|
| samplingFrequencyIndex 	| UB[4] 	| 音频采样率索引值, 44100 对应值 4    	|
| channelConfiguration   	| UB[4] 	| 音频输出声道, 2                     	|
| GASpecificConfig       	|       	|                                     	|
| frameLengthFlag        	| UB[1] 	| 标志位, 用于表明 IMDCT 窗口长度, 0  	|
| dependsOnCoreCoder     	| UB[1] 	| 标志位, 表明是否依赖于 corecoder, 0 	|
| extensionFlag          	| UB[1] 	| 选择了 AAC-LC, 这里必须为 0         	|

在 FLV 的文件中, 一般情况下 AAC sequence header 这种包只出现1次, 而且是第一个 audio tag, 为什么需要这种 tag, 因为在做 FLV demux 的时候, 如果是 AAC 的音频, 需要在每帧 AAC ES 流前边添加 7 个字节 ADST 头, ADST 是解码器通用的格式, 也就是说 AAC 的纯 ES 流要打包成 ADST 格式的 AAC 文件, 解码器才能正常播放. 就是在打包 ADST 的时候, 需要 samplingFrequencyIndex 这个信息, samplingFrequencyIndex 最准确的信息是在 AudioSpecificConfig 中, 这样, 你就完全可以把 FLV 文件中的音频信息及数据提取出来, 送给音频解码器正常播放了.

### VideoTag (E.4.3)

由于 AVC(H.264) 编码的特殊性, 这里着重说明了 AVC(H.264) 编码的 Tag 格式.

| 字段            	| 类型  	| 说明                                                                            	|
|-----------------	|-------	|---------------------------------------------------------------------------------	|
| Video Tag       	|       	|                                                                                 	|
| VideoTagHeader  	|       	|                                                                                 	|
| FrameType       	| UB[4] 	| 1 = key frame, 2 = inter frame                                                  	|
| CodecID         	| UB[4] 	| 7 = AVC                                                                         	|
| AVCPacketType   	| UI8   	| IF CodecID == 7, 0 = AVC sequence header(AVCDecoderConfigurationRecord), 1 = One or more AVC NALUs (Full frames are required), 2 = AVC end of sequence 	|
| CompositionTime 	| SI24  	| IF AVCPacketType == 1 Composition time offset ELSE 0                            	|

VideoTagHeader 的第一个字节, 也就是接跟着 StreamID 的 1 个字节包含着视频帧类型及视频 CodecID 等最基本信息.

VideoTagHeader 之后跟着的就是 VIDEODATA 部分了. 但是, 这里有个特例, 如果视频格式(CodecID)是 AVC, VideoTagHeader 会多出 4 个字节的信息.

AVCDecoderConfigurationRecord 包含着是 H.264 解码相关比较重要的 SPS 和 PPS 信息, 在给 AVC 解码器送数据流之前一定要把 SPS 和 PPS 信息送出,否则的话, 解码器不能正常解码. 而且在解码器 stop 之后再次 start 之前, 如 seek, 快进快退状态切换等, 都需要重新送一遍 SPS 和 PPS 的信息. AVCDecoderConfigurationRecord 在 FLV 文件中一般情况也只出现 1 次, 也就是第一个 video tag.

AVCDecoderConfigurationRecord 长度为 sizeof(UI8) * (11 + sps_size + pps_size)

| 字段                          	| 类型              	| 说明                                  	|
|-------------------------------	|-------------------	|---------------------------------------	|
| AVCDecoderConfigurationRecord 	|                   	|                                       	|
| configurationVersion          	| UI8               	| 版本号, 1                             	|
| AVCProfileIndication          	| UI8               	| SPS[1]                                	|
| profileCompatibility          	| UI8               	| SPS[2]                                	|
| AVCLevelIndication            	| UI8               	| SPS[3]                                	|
| reserved                      	| UB[6]             	| 111111                                	|
| lengthSizeMinusOne            	| UB[2]             	| NALUnitLength - 1, 一般为 3           	|
| reserved                      	| UB[3]             	| 111                                   	|
| numberOfSequenceParameterSets 	| UB[5]             	| SPS 个数, 一般为 1                    	|
| sequenceParameterSetNALUnits  	| UI8[sps_size + 2] 	| sps_size(16bits) + sps(UI8[sps_size]) 	|
| numberOfPictureParameterSets  	| UI8               	| PPS 个数, 一般为 1                    	|
| pictureParameterSetNALUnits   	| UI8[pps_size + 2] 	| pps_size(16bits) + pps(UI8[pps_size]) 	|

### SCRIPTDATA (E.4.4)

ScriptTagBody 内容用 AMF 编码

| 字段            	| 类型            	| 说明                                                     	|
|-----------------	|-----------------	|----------------------------------------------------------	|
| SCRIPTDATA      	|                 	|                                                          	|
| ScriptTagBody   	|                 	|                                                          	|
| Name            	| SCRIPTDATAVALUE 	| Method or object name. SCRIPTDATAVALUE.Type = 2 (String) 	|
| Vale            	| SCRIPTDATAVALUE 	| AMF arguments or object properties.                      	|
| SCRIPTDATAVALUE 	|                 	|                                                          	|
| Type            	| UI8             	| ScriptDataValue 的类型                                   	|
| ScriptDataValue 	| 各种类型        	| Script data 值                                           	|

一个 SCRIPTDATAVALUE 记录包含一个有类型的 ActionScript 值.

### onMetadata (E.5)

FLV metadata object 保存在 SCRIPTDATA 中, 叫 onMetaData. 不同的软件生成的 FLV 的 properties 不同.

| 字段            	| 类型    	| 说明                                                                       	|
|-----------------	|---------	|----------------------------------------------------------------------------	|
| onMetaData      	|         	|                                                                            	|
| audiocodecid    	| Number  	| Audio codec ID used in the file                                            	|
| audiodatarate   	| Number  	| Audio bit rate in kilobits per second                                      	|
| audiodelay      	| Number  	| Delay introduced by the audio codec in seconds                             	|
| audiosamplerate 	| Number  	| Frequency at which the audio stream is replayed                            	|
| audiosamplesize 	| Number  	| Resolution of a single audio sample                                        	|
| canSeekToEnd    	| Boolean 	| Indicating the last video frame is a key frame                             	|
| creationdate    	| String  	| Creation date and time                                                     	|
| duration        	| Number  	| Total duration of the file in seconds                                      	|
| filesize        	| Number  	| Total size of the file in bytes                                            	|
| framerate       	| Number  	| Number of frames per second                                                	|
| height          	| Number  	| Height of the video in pixels                                              	|
| stereo          	| Boolean 	| Indicating stereo audio                                                    	|
| videocodecid    	| Number  	| Video codec ID used in the file (see E.4.3.1 for available CodecID values) 	|
| videodatarate   	| Number  	| Video bit rate in kilobits per second                                      	|
| width           	| Number  	| Width of the video in pixels                                               	|

### keyframes 索引信息

官方的文档中并没有对 keyframes index 做描述, 但是, flv 的这种结构每个 tag 又不像 TS 有同步头, 如果没有 keyframes index 的话, seek 及快进快退的效果会非常差, 因为需要一个 tag 一个 tag 的顺序读取. 后来在做 flv 文件合成的时候, 发现网上有的 flv 文件将 keyframes 信息隐藏在 Script Tag 中. keyframes 几乎是一个非官方的标准, 也就是民间标准.

两个常用的操作 metadata 的工具是 flvtool2 和 FLVMDI, 都是把 keyframes 作为一个默认的元信息项目. 在 FLVMDI 的[主页](http://www.buraks.com/flvmdi/)上有描述:

```
  keyframes: (Object) This object is added only if you specify the /k switch. 'keyframes' is known to FLVMDI and if /k switch is not specified, 'keyframes' object will be deleted.

  'keyframes' object has 2 arrays: 'filepositions' and 'times'. Both arrays have the same number of elements, which is equal to the number of key frames in the FLV. Values in times array are in 'seconds'. Each correspond to the timestamp of the n'th key frame. Values in filepositions array are in 'bytes'. Each correspond to the fileposition of the nth key frame video tag (which starts with byte tag type 9).
```

也就是说 keyframes 中包含着 2 个内容 'filepositions' 和 'times' 分别指的是关键帧的文件位置和关键帧的 PTS. 通过 keyframes 可以建立起自己的 Index, 然后在 seek 和快进快退的操作中, 快速有效地跳转到你想要找的关键帧位置进行处理.

## FLV 分析工具
* <http://www.flvmeta.com/>
* yamdi: 将flv转成带索引的flv, `yamdi -i i.flv -o o.flv`
* flvlib: `pip install flvlib`, 查看索引信息: `debug-flv --metadata file.flv`
* flvcheck: <http://www.adobe.com/products/adobe-media-server-family/tool-downloads.html>

## HTTP-FLV

HTTP-FLV, 即将音视频数据封装成 FLV, 然后通过 HTTP 协议传输给客户端.

这里首先要说一下, HLS 其实是一个 "文本协议", 而并不是一个流媒体协议. 那么, 什么样的协议才能称之为流媒体协议呢?

流(stream): 数据在网络上按时间先后次序传输和播放的连续音/视频数据流. 之所以可以按照顺序传输和播放连续是因为在类似  RTMP, FLV 协议中, 每一个音视频数据都被封装成了包含时间戳信息头的数据包. 而当播放器拿到这些数据包解包的时候能够根据时间戳信息把这些音视频数据和之前到达的音视频数据连续起来播放. MP4, MKV 等等类似这种封装, 必须拿到完整的音视频文件才能播放, 因为里面的单个音视频数据块不带有时间戳信息, 播放器不能将这些没有时间戳信息数据块连续起来, 所以就不能实时的解码播放.

### 延迟分析

理论上(除去网络延迟外), FLV 可以做到仅仅一个音视频 tag 的延迟.

### 相比 RTMP 的优点:

* 可以在一定程度上避免防火墙的干扰 (例如, 有的机房只允许 80 端口通过).
* 可以很好的兼容 HTTP 302 跳转, 做到灵活调度.
* 可以使用 HTTPS 做加密通道.
* 很好的支持移动端(Android, IOS).

### 抓包分析

打开网宿的 HTTP-FLV 流:

<http://175.25.168.16/pl3.live.panda.tv/live_panda/d4e0a83a7e0b0c6e4c5d03774169fa3e.flv?wshc_tag=0&wsts_tag=57e233b1&wsid_tag=6a27c14e&wsiphost=ipdbm>

```
HTTP/1.1 200 OK
Expires: Wed, 21 Sep 2016 07:16:02 GMT
Cache-Control: no-cache
Content-Type: video/x-flv
Pragma: no-cache
Via: 1.1 yc16:3 (Cdn Cache Server V2.0)
Connection: close
```

发现响应头中出现 `Connection: close` 的字段, 表示网宿采用的是短连接, 则直接可以通过服务器关闭连接来确定消息的传输长度.

如果 HTTP Header 中有 Content-Length, 那么这个 Content-Length 既表示实体长度, 又表示传输长度. 而 HTTP-FLV 这种流, 服务器是不可能预先知道内容大小的, 这时就可以使用 `Transfer-Encoding: chunked` 模式来传输数据了.

如下的响应就是采用的Chunked的方式进行的传输的响应头:

```
HTTP/1.1 200 OK
Server: openresty
Date: Wed, 21 Sep 2016 07:38:01 GMT
Content-Type: video/x-flv
Transfer-Encoding: chunked
Connection: close
Expires: Wed, 21 Sep 2016 07:38:00 GMT
Cache-Control: no-cache
```
