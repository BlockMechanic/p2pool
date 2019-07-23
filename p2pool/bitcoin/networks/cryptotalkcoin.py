import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f7bad4a9'.decode('hex')
P2P_PORT = 8383
ADDRESS_VERSION = 28
RPC_PORT = 8444
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '01e3261a8c1267086ddcfbb36a969f0382b446998b99c5f6f52279702dd7a8d8')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: (5*100000000 >> (height + 1)//210000)
POW_FUNC = data.hash256momentum
BLOCK_PERIOD = 60 # s
SYMBOL = 'CRT'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Cryptotalkcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Cryptotalkcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.cryptotalkcoin'), 'cryptotalkcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/crt/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/crt/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/crt/tx.dws?'
SANE_TARGET_RANGE = (2**256//2**7//1000000000 - 1, 2**256//2**7 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
