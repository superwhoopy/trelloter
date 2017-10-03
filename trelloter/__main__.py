import sys

from . import leboncoin
from . import trello

if __name__ == '__main__':
    ad = leboncoin.parse_page(sys.argv[1])
    trello.register_ad(ad)
