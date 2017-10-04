from collections import namedtuple

_Ad = namedtuple('Ad', ['price', 'surface', 'town', 'atype', 'rooms', 'img',
                       'url'])

class Ad(_Ad):
    def short(self):
        return "{atype} {rooms}P {surface} {town}, {price}".format(
            atype=self.atype, rooms=self.rooms, surface=self.surface,
            town=self.town, price=self.price)

    def __str__(self):
        lineformat = "{:10} {}"
        lines = []
        lines.append(lineformat.format("Type :", self.atype))
        lines.append(lineformat.format("Surface :", self.surface))
        lines.append(lineformat.format("Ville :", self.town))
        lines.append(lineformat.format("Prix :", self.price))
        lines.append(lineformat.format("Chambres :", self.rooms))
        lines.append(lineformat.format("Image :", self.img))
        lines.append(lineformat.format("URL :", self.url))
        return '\n'.join(lines)
