# TODO:
- https://github.com/tromgy/service-base
- https://github.com/chfast/ethash


# Algorithm
| miner | algo |
|---|---| 
| cpu | ethash |
| opencl | ? |
| cuda | ethash |
| metal | TODO: |


## 结构
```txt
                                       libfminer.a
                                      /
fminer UI --- start/stop ---> Service
                                      \
                                       libhw.a
```

## Service
TODO:

### Service Control
- Install
- Start
- Stop
- Query status

### Json RPC API
