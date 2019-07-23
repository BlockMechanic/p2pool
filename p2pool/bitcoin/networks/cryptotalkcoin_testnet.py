import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '0b110907'.decode('hex')
P2P_PORT = 18333
ADDRESS_VERSION = 111
RPC_PORT = 18332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitcreditaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//21000
POW_FUNC = data.hash256momentum
BLOCK_PERIOD = 600 # s
SYMBOL = 'tBCR'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcredit') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcredit/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcredit'), 'bitcredit.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://trc.cryptocoinexplorer.com/testnet/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://trc.cryptocoinexplorer.com/testnet/address/'
TX_EXPLORER_URL_PREFIX = 'http://trc.cryptocoinexplorer.com/testnet/tx/'
SANE_TARGET_RANGE = (2**256//2**4//1000000000 - 1, 2**256//2**4 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
