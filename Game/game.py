from Objects import Town
from Objects.Items import Item, Equipment


class Game(object):
    towns: [Town]
    items: [Item]
    equipments: [Equipment]

    def __init__(self, *args, **kwargs):
        pass

    def generate_towns(self):
        pass

    def create_or_update_town(self):
        pass

    def generate_items(self):
        pass

    def create_or_update_item(self):
        pass

    def generate_equipment(self):
        pass

    def create_or_update_equipment(self):
        pass
