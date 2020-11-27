"""
Model
"""

import basic_backend as bb


class ModelBasic:
    def __init__(self, application_items):
        self._item_type = 'product'
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_item(self, name, price, quantity):
        bb.create_item(name, price, quantity)

    def create_items(self, items):
        bb.create_items(items)

    def read_item(self, name):
        return bb.read_item(name)

    def read_items(self):
        return bb.read_items()

    def update_item(self, name, price, quantity):
        bb.update_item(name, price, quantity)

    def delete_item(self, name):
        bb.delete_item(name)
