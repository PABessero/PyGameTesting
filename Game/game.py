from Objects import Town
from Objects.Items import Item, Equipment


class Game(object):
    towns: [Town] = []
    items: [Item] = []
    equipments: [Equipment] = []

    def __init__(self, *args, **kwargs):
        pass

    def generate_towns(self):
        pass

    def create_or_update_town(self, town_id: str, name: str, base_class: str = 'test_game'):
        if town_id in self.towns:
            pass
        else:
            self.towns.append(Town(town_id, name))

    def generate_items(self):
        pass

    def create_or_update_item(self):
        pass

    def generate_equipment(self):
        pass

    def create_or_update_equipment(self):
        pass
