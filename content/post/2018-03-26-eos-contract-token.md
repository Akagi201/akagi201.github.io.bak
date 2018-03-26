+++
date = "2018-03-26T13:46:50+08:00"
title = "EOS 合约开发之 token"
slug = "eos-contract-token"

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

* 为 `token` 合约创建账户.
* 创建 `owner_key`: `cleos create key`

```
root@199345c94897:~# cleos create key
Private key: 5JBrL9JTBxooBAxCU41PEXX1hFpPiPiCVH6PyFAtqEMAKNw8gwT
Public key: EOS6rgmK4g6L8nu7y2tXnfk4F8JZctZ5QKkvga3CAsfv9DFfLFmr1
```

* 创建 `active_key`: `cleos create key`

```
root@199345c94897:~# cleos create key
Private key: 5K6bPikRThnWYM6XgvaWdezJrri1RRjoEthfZcUPvekHNKMyrX6
Public key: EOS4xAHcZfLjXbBiLYYYhohXjFyC2Ct45sc5hTRMCGyYRKbLyyNLD
```

* 创建 `token` 账户.

```
root@199345c94897:~# cleos create account eosio token EOS6rgmK4g6L8nu7y2tXnfk4F8JZctZ5QKkvga3CAsfv9DFfLFmr1 EOS4xAHcZfLjXbBiLYYYhohXjFyC2Ct45sc5hTRMCGyYRKbLyyNLD
{
  "transaction_id": "103744a19981c7bd08e5b33e00d6fbca73a9b5f34ed062700f625fa8c3048379",
  "processed": {
    "status": "executed",
    "id": "103744a19981c7bd08e5b33e00d6fbca73a9b5f34ed062700f625fa8c3048379",
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
          "data": "0000000000ea30550000000080a920cd01000000010003034c349df8bdaa38b98ca9911c3a26fd9b6d1d7af167b2eb5c3a287cf09f4b570100000100000001000208560867098550d4c51c4e62dedc1192906e7e83cbb406d3d9b7d726d9833eed0100000100000000010000000000ea305500000000a8ed32320100"
        },
        "console": "",
        "region_id": 0,
        "cycle_index": 0,
        "data_access": [{
            "type": "write",
            "code": "eosio",
            "scope": "eosio.auth",
            "sequence": 3
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
root@199345c94897:~# cleos get account token
{
  "account_name": "token",
  "permissions": [{
      "perm_name": "active",
      "parent": "owner",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS4xAHcZfLjXbBiLYYYhohXjFyC2Ct45sc5hTRMCGyYRKbLyyNLD",
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
            "key": "EOS6rgmK4g6L8nu7y2tXnfk4F8JZctZ5QKkvga3CAsfv9DFfLFmr1",
            "weight": 1
          }
        ],
        "accounts": []
      }
    }
  ]
}
```

* 导入 `token` 账户 active private key.

```
cleos wallet import 5K6bPikRThnWYM6XgvaWdezJrri1RRjoEthfZcUPvekHNKMyrX6
```

## 上传 `token` 合约到区块链
* 验证 `token` 账户没有部署合约.

```
root@199345c94897:~# cleos get code token
code hash: 0000000000000000000000000000000000000000000000000000000000000000
```

* 上传合约, 来的 `/tmp/build` 目录下

```
root@199345c94897:~# cd /tmp/build
root@199345c94897:~# cleos set contract token contracts/eosio.token/eosio.token.wast contracts/eosio.token/eosio.token.abi

```

* 查看合约地址

```
root@199345c94897:/tmp/build# cleos get code token
code hash: 78807447a2cb04645b82125d9e4f499e0c262d018514cfa8f77bfb5e57c8e7a4
{
  "transaction_id": "3928a42f0132b6d48738e3f1f69b2739f1ffe73c0778f95bed6156d4e1ff1456",
  "processed": {
    "status": "executed",
    "id": "3928a42f0132b6d48738e3f1f69b2739f1ffe73c0778f95bed6156d4e1ff1456",
    "action_traces": [{
        "receiver": "eosio",
        "act": {
          "account": "eosio",
          "name": "setcode",
          "authorization": [{
              "actor": "token",
              "permission": "active"
            }
          ],
          "data": "0000000080a920cd000089a2010061736d010....20616c6c6f636174656400"
        },
        "console": "",
        "region_id": 0,
        "cycle_index": 0,
        "data_access": [{
            "type": "write",
            "code": "eosio",
            "scope": "eosio.auth",
            "sequence": 4
          }
        ]
      },{
        "receiver": "eosio",
        "act": {
          "account": "eosio",
          "name": "setabi",
          "authorization": [{
              "actor": "token",
              "permission": "active"
            }
          ],
          "data": "0000000080a920cd010c6163636f756e745f6e616d65046e616d6505087472616e7366657200040466726f6d0c6163636f756e745f6e616d6502746f0c6163636f756e745f6e616d65087175616e74697479056173736574046d656d6f06737472696e67066372656174650005066973737565720c6163636f756e745f6e616d650e6d6178696d756d5f737570706c790561737365740a63616e5f667265657a650575696e74380a63616e5f726563616c6c0575696e74380d63616e5f77686974656c6973740575696e7438056973737565000302746f0c6163636f756e745f6e616d65087175616e74697479056173736574046d656d6f06737472696e67076163636f756e7400020863757272656e63790675696e7436340762616c616e63650675696e7436340e63757272656e63795f737461747300020863757272656e63790675696e74363406737570706c790675696e74363403000000572d3ccdcd087472616e736665720000000000a5317605697373756500000000a86cd4450663726561746502000000204f4d113203693634010863757272656e6379010675696e743634076163636f756e740000000000904dc603693634010863757272656e6379010675696e7436340e63757272656e63795f7374617473"
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

## 测试 token 合约

* create

```
cleos push action token create '{"issuer":"token", "maximum_supply": "1000000000.0000 CUR", "can_freeze": 1, "can_recall": 1, "can_whitelist": 1}' -p token@active
```

* issue

```
cleos push action token issue '{"to":"token","quantity":"1000.0000 CUR","memo":"issue"}' --permission token@active
```

* transfer

```
cleos push action token transfer '{"from":"token","to":"eosio","quantity":"20.0000 CUR","memo":"my first transfer"}' --permission token@active
```

## 查看转账后账户 balance

> 注意目前 master 分支 table 有 bug, 等待官方进行 fix.

* 查看 eosio 账户:

```
cleos get table eosio token account
```

* 查看 token 账户:

```
cleos get table token token account
```
