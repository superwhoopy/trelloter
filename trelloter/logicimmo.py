import logging
import enum

from lxml import etree

from .annonce import Ad

log = logging.getLogger(__name__)

def sanitize(text):
    return text.strip().encode().decode()

def parse_page(html, httpurl=None):
    root = etree.HTML(html) #pylint: disable=no-member

    price = root.xpath("//h2[@class='main-price']")[0]
    price = sanitize(price.text)

    surface = root.xpath("//span[@class='offer-area-number']")[0]
    surface = sanitize(surface.text)

    rooms = root.xpath("//span[@class='offer-rooms-number']")[0]
    rooms = sanitize(rooms.text)

    town = root.xpath("//div[@class='cell locality']")[0]
    town = next(town.iterchildren())
    town = sanitize(town.text)

    atype = root.xpath("//div[@class='cell type']")[0]
    atype = next(atype.iterchildren())
    atype = sanitize(atype.text)

    img = root.xpath("//img[@id='offer_pictures_main']")
    img = img[0].attrib['src']

    return Ad(price, surface, town, atype, rooms, img, httpurl)
