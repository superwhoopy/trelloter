import logging
import enum
import urllib.request

from lxml import etree

from .annonce import Ad

log = logging.getLogger(__name__)

class Items(enum.Enum):
    PRIX         = "Prix"
    VILLE        = ''
    FRAIS_AGENCE = 'Frais'
    TYPE         = 'Type de bien'
    PIECES       = 'Pièces'
    SURFACE      = 'Surface'

def parse_page(httpurl):
    try:
        with urllib.request.urlopen(httpurl) as response:
            html = response.read()
    except urllib.error.URLError:
        log.error("cannot reach url " + httpurl)
        return

    root = etree.HTML(html) #pylint: disable=no-member
    props = root.xpath("//span[@class='property']")
    vals = root.xpath("//span[@class='value']")
    img = root.xpath("//meta[@property='og:image']")

    props = [x.text.strip().encode().decode() for x in props]
    vals = [x.text.strip().encode().decode() for x in vals]
    log.debug("props: {}".format(props))
    log.debug("vals: {}".format(vals))
    log.debug("img: {}".format(img[0].attrib['content']))

    props_dict = {}
    for prop, val in zip(props, vals):
        for item in Items:
            if prop == item.value:
                props_dict[item.name] = val

    log.debug("props_dict: {}".format(props_dict))

    ad = Ad(props_dict[Items.PRIX.name],
            props_dict[Items.SURFACE.name],
            props_dict[Items.VILLE.name],
            atype=props_dict[Items.TYPE.name],
            rooms=props_dict[Items.PIECES.name],
            img=img[0].attrib['content'],
            url=httpurl)

    return ad
