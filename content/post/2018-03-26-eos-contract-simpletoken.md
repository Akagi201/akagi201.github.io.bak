+++
date = "2018-03-26T13:46:50+08:00"
title = "EOS 合约开发"
slug = "eos-contract-simpletoken"

+++

## 开发环境
使用 [eos/builder](http://hub.docker.com/r/eosio/builder) 作为开发环境, 使用 master 分支最新代码.

## 启动 EOS 单节点

* 在一个终端启动 `nodeosd.sh`, 可以看到不断有区块产生, 后续操作在另一个终端中进行.
* 通过 `get info` api, 来检查是否运行正常

```
root@199345c94897:~# http get http://127.0.0.1:8888/v1/chain/get_info
HTTP/1.1 200 OK
Content-Length: 235
Content-type: application/json
Server: WebSocket++/0.7.0

{
    "head_block_id": "000000418661452eb2d425d0f1caed204af15d117bbf4ab1c82764235aff6d62",
    "head_block_num": 65,
    "head_block_producer": "eosio",
    "head_block_time": "2018-03-26T06:03:48",
    "last_irreversible_block_num": 64,
    "server_version": "83f6ce54"
}
```

## 创建钱包以及账户

* 创建钱包 `cleos wallet create`

```
root@199345c94897:~# cleos wallet create
Creating wallet: default
Save password to use in the future to unlock this wallet.
Without password imported keys will not be retrievable.
"PW5Jg1u5EuNpcMiTMqM78a6NVbvNd9CHnYa39Mfu3TZ35XQvQZeur"
```

* 导入 `eosio` 系统账户的 private key, 保存在 genesis.json.`cleos wallet import 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3`

```
root@199345c94897:~# cleos wallet import 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
imported private key for: EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
```

* 为 `simpletoken` 合约创建账户.
* 创建 `owner_key`: `cleos create key`

```
root@199345c94897:~# cleos create key
Private key: 5KjF7xAaMwgohSsMcZZb5cZkkwE6CCZ9ZniXSdLyPsAVNVRgA7Z
Public key: EOS6fJP65V19He76SSqttK6hSGEeXZnYnXxWQeqQsEKptAN3KEbXF
```

* 创建 `active_key`: `cleos create key`

```
root@199345c94897:~# cleos create key
Private key: 5JqJ6KcyufUsCAEhK9K6MMdd68s9UsvjEczbtcurbWueLsk7CBq
Public key: EOS6bV9M1zCWATVhA2f5ANSBT91L1fhoSnHnyGapKVzgAiRF1D9UB
```

* 创建 `simpletoken` 账户.

```
root@199345c94897:~# cleos create account eosio simpletoken EOS6fJP65V19He76SSqttK6hSGEeXZnYnXxWQeqQsEKptAN3KEbXF EOS6bV9M1zCWATVhA2f5ANSBT91L1fhoSnHnyGapKVzgAiRF1D9UB
{
  "transaction_id": "e960ff39c06752e8aa55ef443cfbf0e40c02b502a95cf1c2214715b0d579c313",
  "processed": {
    "status": "executed",
    "id": "e960ff39c06752e8aa55ef443cfbf0e40c02b502a95cf1c2214715b0d579c313",
    "action_traces": [{
        "receiver": "eosio",
        "act": {
          "account": "eosio",
          "name": "newaccount",
          "authorization": [{
              "actor": "eosio",
              "permission": "active"
            }
          ],
          "data": "0000000000ea305500a68234ab58a5c301000000010002e971cec0c9bcf7da636948d1b1060111bd92a53cd4a3ed5661253e17cff7c26e01000001000000010002e0c88ef207a0499bfd5af39b9d173046d3562525da6a03c99d3074ec151f0c8d0100000100000000010000000000ea305500000000a8ed32320100"
        },
        "console": "",
        "region_id": 0,
        "cycle_index": 0,
        "data_access": [{
            "type": "write",
            "code": "eosio",
            "scope": "eosio.auth",
            "sequence": 1
          }
        ]
      }
    ],
    "deferred_transactions": []
  }
}
```

* 获取账户信息 `cleos get account`

```
root@199345c94897:~# cleos get account simpletoken
{
  "account_name": "simpletoken",
  "permissions": [{
      "perm_name": "active",
      "parent": "owner",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS6bV9M1zCWATVhA2f5ANSBT91L1fhoSnHnyGapKVzgAiRF1D9UB",
            "weight": 1
          }
        ],
        "accounts": []
      }
    },{
      "perm_name": "owner",
      "parent": "",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS6fJP65V19He76SSqttK6hSGEeXZnYnXxWQeqQsEKptAN3KEbXF",
            "weight": 1
          }
        ],
        "accounts": []
      }
    }
  ]
}
```

* 导入 `simpletoken` 账户 active private key.

```
cleos wallet import 5JqJ6KcyufUsCAEhK9K6MMdd68s9UsvjEczbtcu
```

## 上传 `simpletoken` 合约到区块链
* 验证 `simpletoken` 账户没有部署合约.

```
root@199345c94897:~# cleos get code simpletoken
code hash: 0000000000000000000000000000000000000000000000000000000000000000
```

* 上传合约, 来的 `/tmp/build` 目录下

```
root@199345c94897:~# cd /tmp/build
root@199345c94897:~# cleos set contract currency contracts/simple.token/simple.token.wast contracts/simple.token/simple.token.abi
{
  "transaction_id": "38cbc427893ef25366589941fffd39e95938988c645289e26b203b9ff9681207",
  "processed": {
    "status": "executed",
    "id": "38cbc427893ef25366589941fffd39e95938988c645289e26b203b9ff9681207",
    "action_traces": [{
        "receiver": "eosio",
        "act": {
          "account": "eosio",
          "name": "setcode",
          "authorization": [{
              "actor": "simpletoken",
              "permission": "active"
            }
          ],
          "data": "00a68234ab58a5c30000813d0061736d010000000....656400"
        },
        "console": "",
        "region_id": 0,
        "cycle_index": 0,
        "data_access": [{
            "type": "write",
            "code": "eosio",
            "scope": "eosio.auth",
            "sequence": 2
          }
        ]
      },{
        "receiver": "eosio",
        "act": {
          "account": "eosio",
          "name": "setabi",
          "authorization": [{
              "actor": "simpletoken",
              "permission": "active"
            }
          ],
          "data": "00a68234ab58a5c300000000"
        },
        "console": "",
        "region_id": 0,
        "cycle_index": 0,
        "data_access": []
      }
    ],
    "deferred_transactions": []
  }
}
```

* 查看合约地址

```
root@199345c94897:/tmp/build# cleos get code simpletoken
code hash: 78807447a2cb04645b82125d9e4f499e0c262d018514cfa8f77bfb5e57c8e7a4
```

## 测试 simpletoken 合约

* issue

```
cleos push action simpletoken issue '{"to":"simpletoken","quantity":"1000","memo":"issue"}' --permission simpletoken@active
```

* transfer

```
cleos push action simpletoken transfer '{"from":"simpletoken","to":"eosio","quantity":"20","memo":"my first transfer"}' --permission simpletoken@active
```

## 查看转账后账户 balance

* 查看 eosio 账户:

```
cleos get table eosio simpletoken account
```

* 查看 simpletoken 账户:

```
cleos get table simpletoken simpletoken account
```
