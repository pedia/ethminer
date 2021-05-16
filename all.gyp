# CLI11 639a8a
# jsoncpp 1.8.1
{
  'target_defaults': {
    'xcode_settings': {
      'CC': 'clang++',
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++0x',
      'ARCHS': ['x86_64'],
    },
  },
  'targets': [
    {
      'include_dirs': [
        '.',
        '../boost_1_76_0',
        'ethash/include',
        'ethash/include/ethash',
        'jsoncpp/include',
        '/usr/local/opt/openssl/include',  # openssl
        'CLI11/include',
      ],
      'target_name': 'ethminer',
      'type': 'executable',
      'dependencies': [
        'ethash',
        'jsoncpp',
      ],
      'defines': [
        # 'ETH_ETHASHCL',
        # 'ETH_ETHASHCUDA',
        'ETH_ETHASHCPU',
        'API_CORE',
      ],
      'library_dirs': [
        '../boost_1_76_0/stage/lib',
        '/usr/local/opt/openssl@1.1/lib',
      ],
      'libraries': [
        '-lboost_filesystem',
        '-lboost_system',
        '-lboost_thread',
        '-lstdc++',
        '-lm',
        '-lcrypto',
        '-lssl',
        # '-lOpenCL',
        # 'OpenCL.framework',
      ],
      'mac_framework_dirs': [
        '/System/Library/PrivateFrameworks',
        '/System/Library/Frameworks',
        '$(SDKROOT)/System/Library/Frameworks/Foundation.framework'
      ],
      'link_settings': {
        'libraries': [
          '$(SDKROOT)/System/Library/Frameworks/OpenCL.framework',
        ]
      },
      'sources': [
        # 'libethash-cl/CLMiner.cpp',
        'libethcore/EthashAux.cpp',
        'libethcore/Farm.cpp',
        'libethcore/Miner.cpp',
        'libdevcore/Log.cpp',
        'libdevcore/Worker.cpp',
        'libdevcore/CommonData.cpp',
        'libdevcore/FixedHash.cpp',
        'ethminer/main.cpp',
        'libhwmon/wrapnvml.cpp',
        'libhwmon/wrapadl.cpp',
        'libhwmon/wraphelper.cpp',
        'libhwmon/wrapamdsysfs.cpp',
        # 'libethash-cuda/CUDAMiner.cpp',
        'libethash-cpu/CPUMiner.cpp',
        'libapicore/ApiServer.cpp',
        'libpoolprotocols/PoolURI.cpp',
        'libpoolprotocols/stratum/EthStratumClient.cpp',
        'libpoolprotocols/testing/SimulateClient.cpp',
        'libpoolprotocols/PoolManager.cpp',
        'libpoolprotocols/getwork/EthGetworkClient.cpp',
      ],
      'xcode_settings': {
        # 'MACOSX_DEPLOYMENT_TARGET': '10.9',
        'CLANG_CXX_LIBRARY': 'libc++',
      },
    },
    {
      'include_dirs': ['ethash/include',],
      'target_name': 'ethash',
      'type': 'static_library',
      'sources': [
        'ethash/lib/ethash/progpow.cpp',
        'ethash/lib/ethash/ethash.cpp',
        'ethash/lib/ethash/managed.cpp',
        'ethash/lib/keccak/keccak.c',
        'ethash/lib/keccak/keccakf800.c',
        'ethash/lib/ethash/primes.c',
      ],
    },
    {
      'include_dirs': ['jsoncpp/include',],
      'target_name': 'jsoncpp',
      'type': 'static_library',
      'sources': [
        'jsoncpp/src/lib_json/json_reader.cpp',
        'jsoncpp/src/lib_json/json_value.cpp',
        'jsoncpp/src/lib_json/json_writer.cpp',
      ],
    },
    # {
    #   'target_name': 'metal_test',
    #   'type': 'executable',
    #   'mac_bundle': 1,
    #   'sources': [
    #     'metal_test.cc',
    #   ],
    #   'link_settings': {
    #     'libraries': [
    #       '$(SDKROOT)/System/Library/Frameworks/OpenCL.framework',
    #     ],
    #   },
    # },
  ],
}
