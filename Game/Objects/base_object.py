class BaseObject(object):
    base_class: str
    id: str
    name: str

    def __init__(self, id_: str, name: str, base_class: str = 'test_game'):
        self.id = id_
        self.name = name
        self.base_class = base_class

    def __str__(self):
        return self.base_class + ':' + self.id
