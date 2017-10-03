import sys
import urllib.request
import enum

from lxml import etree

from annonce import Ad

class Items:
    PRIX         = 0
    VILLE        = 1
    FRAIS_AGENCE = 2
    TYPE         = 3
    PIECES       = 4
    SURFACE      = 5

def parse_page(html):
    root = etree.HTML(html) #pylint: disable=no-member
    # props = root.xpath("//span[@class='property']")
    vals = root.xpath("//span[@class='value']")
    img = root.xpath("//meta[@property='og:image']")

    ad = Ad(vals[Items.PRIX].text.strip().encode().decode(),
            vals[Items.SURFACE].text.strip(),
            vals[Items.VILLE].text.strip(),
            atype=vals[Items.TYPE].text.strip(),
            rooms=vals[Items.PIECES].text.strip(),
            img=img[0].attrib['content'])

    print(str(ad))

def read_page(httpurl):
    with urllib.request.urlopen(httpurl) as response:
        html = response.read()
    parse_page(html)

if __name__ == '__main__':
    read_page(sys.argv[1])
