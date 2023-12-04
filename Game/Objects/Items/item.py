from Game.Objects import BaseObject


class Item(BaseObject):

    def __init__(self, id_: str, name: str, *args, **kwargs):
        super().__init__(id_, name)
