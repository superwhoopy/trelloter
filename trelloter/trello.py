import trello

from . import annonce

TRELLO_KEY = 'f8b22befcd70f239ba9c9971694da1a5'
TRELLO_TOKEN = '62cec75820784545232977b200943d5aa32f622122355a85492dc11506c16806'

BOARD_APPART = '58cf886abe89030dafe85432'
LIST_CONTACT = '58cf88704ca8bc50a99948f9'

def register_ad(ad):
    title = ad.desc()
    desc = "bar"
    card_handler = trello.Cards(TRELLO_KEY, token=TRELLO_TOKEN)
    card = card_handler.new(title, LIST_CONTACT, desc=desc)
    card_handler.new_attachment(card['id'], ad.img, 'Image')
    card_handler.new_attachment(card['id'], ad.url, 'URL')

def test_register_ad():
    ad = annonce.Ad('0eur', '0 m2', 'Tombouctou', 'Palace', '0',
                    'http://tamere', 'http://fuckyou')
    register_ad(ad)
