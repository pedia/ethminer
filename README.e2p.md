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
# cpu temperature
| system | code |
|---|---|
| mac | https://github.com/lavoiesl/osx-cpu-temp |
| linux | https://github.com/shibatch/cputemp |
| windows/nvidia | https://github.com/openhardwaremonitor/openhardwaremonitor/blob/master/Hardware/Nvidia/NVAPI.cs |
