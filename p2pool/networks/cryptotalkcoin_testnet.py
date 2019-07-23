from p2pool.bitcoin import networks

PARENT = networks.nets['bitcredit_testnet']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 60*60//15 # shares
REAL_CHAIN_LENGTH = 60*60//15 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 20 # blocks
IDENTIFIER = 'b1dc7ed1dc11e0d2'.decode('hex')
PREFIX = 'ba0c05e7ad100302'.decode('hex')
P2P_PORT = 18777
MIN_TARGET = 0
MAX_TARGET = 2**256//2**4 - 1
PERSIST = False
WORKER_PORT = 18776
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-bcr-alt'
VERSION_CHECK = lambda v: 300700 <= v
