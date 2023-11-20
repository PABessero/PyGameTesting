from base_object import BaseObject


class Item(BaseObject):
    def __init__(self, id_: str, name: str):
        super().__init__(id_, name)
