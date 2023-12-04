from item import Item


class Resource(Item):

    def __init__(self, id_: str, name: str, *args, **kwargs):
        super().__init__(id_, name)
