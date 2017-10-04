
class Ad(object):

    def __init__(self, price, surface, town, atype, rooms, img, url):
        self.price = self.stringify(price, 'eur')
        self.surface = self.stringify(surface, 'm2')
        self.town = town
        self.atype = atype
        self.rooms = self.stringify(rooms, 'P')
        self.img = img
        self.url = url

    @staticmethod
    def stringify(intarg, suffix):
        try:
            intval = int(intarg)
        except ValueError:
            return intarg
        return "{}{}".format(intval, suffix)

    def short(self):
        return "{atype} {rooms} {surface} {town}, {price}".format(
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
