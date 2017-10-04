import argparse
import logging
import textwrap
from collections import namedtuple

from . import leboncoin
from . import trellopost

Parser = namedtuple('Parser', ['domain', 'parsefunc'])

PARSERS = (
    Parser("leboncoin.fr", leboncoin.parse_page),
)

def main():
    parser = argparse.ArgumentParser(prog='trelloter')
    parser.add_argument('url', nargs='+')
    parser.add_argument('-d', '--debug', help='Debug mode', action='store_true')
    parser.add_argument('--dry', help='Do not create a Trello card',
                        action='store_true')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    for url in args.url:
        parser = [parse_func for domain, parse_func in PARSERS
                             if url.find(domain) != -1]
        if not parser:
            logging.error('cannot find a parser for url "{}"'.format(url))
            return
        assert len(parser) == 1
        parser = parser[0]

        logging.info("Fetching ad from '{}'".format(url))
        ad = leboncoin.parse_page(url)
        # ad = annonce.Ad('0eur', '0 m2', 'Tombouctou', 'Palace', '0',
        #                 'http://tamere', 'http://fuckyou')
        logging.info("Registering this ad:\n" + textwrap.indent(str(ad), '  '))
        logging.debug("Title: '{}'".format(ad.short()))
        if not args.dry:
            trellopost.register_ad(ad)
        else:
            logging.info("Dry run: skipped registration")
        logging.info("Done")

if __name__ == '__main__':
    main()
