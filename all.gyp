# CLI11 639a8a
# jsoncpp 1.8.1
# ethash master

# gyp --depth=. -f ninja all.gyp && ninja -C out/Default
{
    'target_defaults': {
    'xcode_settings': {
      'CC': 'clang++',
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++0x',
      'ARCHS': ['x86_64'],
    },
    'configurations': {
      'msvs_configuration_attributes': {
        'CharacterSet': '1'
      },
      'Debug_x64': {
        'msvs_configuration_platform': 'x64',
        'defines': [
            'DEBUG',
            'WINDOWS',
            # 'AP_ENGINE_CLIENT_BACKEND',
        ],
        'include_dirs': [
        ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': '3', # /MDd
            'Optimization': '0',
          },
        },
      },
      'Release_x64': {
        'msvs_configuration_platform': 'x64',
        'defines': [
            'NDEBUG',
            'WINDOWS',
            # 'AP_ENGINE_CLIENT_BACKEND',
        ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': '2' # /MD
          },
          'VCLinkerTool': {
            'GenerateDebugInformation': 'true',
          },
        },
      },
    },
  },

  'targets': [
    {
      'target_name': 'ethminer',
      'include_dirs': [
        '.',
        '../boost_1_76_0',
        'ethash/include',
        'ethash/include/ethash',
        'thirdparty/jsoncpp/include',
        '/usr/local/opt/openssl/include',  # openssl
        'thirdparty/CLI11/include',
      ],
      'type': 'executable',
      'dependencies': [
        'core',
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
        'ethminer/main.cpp',
      ],
      'xcode_settings': {
        'CLANG_CXX_LIBRARY': 'libc++',
      },
    },
    ##########
    {
      'target_name': 'fminer',
      'type': 'shared_library',
      'include_dirs': [
        '.',
        '../boost_1_76_0',
        'ethash/include',
        'ethash/include/ethash',
        'thirdparty/jsoncpp/include',
        '/usr/local/opt/openssl/include',  # openssl
        'thirdparty/CLI11/include',
      ],
      'dependencies': [
        'core',
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
        'ethminer/main.cpp',
      ],
      'xcode_settings': {
        'CLANG_CXX_LIBRARY': 'libc++',
      },
    },
    ##########
    {
      'target_name': 'core',
      'type': 'static_library',
      'include_dirs': [
        '.',
        '../boost_1_76_0',
        'ethash/include',
        'ethash/include/ethash',
        'thirdparty/jsoncpp/include',
        '/usr/local/opt/openssl/include',  # openssl
        'thirdparty/CLI11/include',
      ],
      'defines': [
        # 'ETH_ETHASHCL',
        # 'ETH_ETHASHCUDA',
        'ETH_ETHASHCPU',
        'API_CORE',
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
        # 'ethminer/main.cpp',
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
        'CLANG_CXX_LIBRARY': 'libc++',
      },
    },
    {
      'target_name': 'ethash',
      'include_dirs': ['ethash/include',],
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
      'target_name': 'jsoncpp',
      'type': 'static_library',
      'include_dirs': ['thirdparty/jsoncpp/include',],
      'sources': [
        'thirdparty/jsoncpp/src/json_reader.cpp',
        'thirdparty/jsoncpp/src/json_value.cpp',
        'thirdparty/jsoncpp/src/json_writer.cpp',
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
