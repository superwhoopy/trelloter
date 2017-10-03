from collections import namedtuple

_Ad = namedtuple('Ad', ['price', 'surface', 'town', 'atype', 'rooms', 'img',
                       'url'])

class Ad(_Ad):
    def desc(self):
        return "{atype} {rooms}P {surface}m2 {town}, {price}".format(
            atype=self.atype, rooms=self.rooms, surface=self.surface,
            town=self.town, price=self.price)
