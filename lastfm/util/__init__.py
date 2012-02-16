__author__ = "Abhinav Sarkar <abhinav@abhinavsarkar.net>"
__version__ = "0.2"
__license__ = "GNU Lesser General Public License"
__package__ = "lastfm.util"

from lastfm.util.wormhole import Wormhole
from lastfm.util._lazylist import lazylist
from lastfm.util.safelist import SafeList
from lastfm.util.filecache import FileCache
from lastfm.util.objectcache import ObjectCache
from dateutil import zoneinfo

__all__ = ['Wormhole', 'lazylist', 'SafeList',
           'FileCache', 'ObjectCache', 'UTC']

UTC = zoneinfo.gettz('UTC')

def safe_int(integer):
    try:
        return int(integer)
    except ValueError:
        return 0

def safe_float(floatish):
    try:
        return int(floatish)
    except ValueError:
        return 0
