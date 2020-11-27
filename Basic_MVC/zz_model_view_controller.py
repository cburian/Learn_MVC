import basic_backend as bb
import mvc_exceptions as m_ex


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


class View:

    @staticmethod
    def show_bullet_point_list(item_type, items):
        print(f'--- {item_type.upper()} ---')
        for item in items:
            print(f'* {item}')

    @staticmethod
    def show_number_point_list(item_type, items):
        print(f'--- {item_type.upper()} ---')
        for i, item in enumerate(items):
            print(f'{i + 1}. {item}')

    @staticmethod
    def show_item(item_type, item, item_info):
        print('/'*30)
        print(f'We have some {item.upper()}!')
        print(f'{item_type.upper()} INFO: {item_info}')
        print('/' * 30)

    @staticmethod
    def display_missing_item_error(item, err):
        print('*' * 30)
        print(f'We don\'t have {item.upper()}!')
        print(f'{err.args[0]}')
        print('*' * 30)

    @staticmethod
    def display_item_already_stored_error(item, item_type, err):
        print('*' * 30)
        print(f'We already have {item.upper()} in our {item_type} list!')
        print(f'{err.args[0]}')
        print('*' * 30)

    @staticmethod
    def display_item_not_yet_stored_error(item, item_type, err):
        print('*' * 30)
        print(f'We don\'t have any {item.upper()} in our {item_type} list!')
        print(f'{err.args[0]}')
        print('*' * 30)

    @staticmethod
    def display_item_stored(item, item_type):
        print('+' * 30)
        print(f'We just added {item.upper()} in our {item_type} list')
        print('+' * 30)

    @staticmethod
    def display_change_item_type(older, newer):
        print('--- ' * 6)
        print(f'Changed item type from {older} to {newer}!')
        print('--- ' * 6)

    @staticmethod
    def display_item_update(item, o_price, o_quantity, n_price, n_quantity):
        print('--- ' * 6)
        print(f'Changed {item} price: {o_price} --> {n_price}!')
        print(f'Changed {item} quantity: {o_quantity} --> {n_quantity}!')
        print('--- ' * 6)

    @staticmethod
    def display_item_deletion(name):
        print('-' * 30)
        print(f'We just removed {name} from our list')
        print('-' * 30)


class Controller:

    def __init__(self, model: ModelBasic, view: View):
        self.model = model
        self.view = view

    def show_items(self, bullet_points = False):
        items = self.model.read_items()
        item_type = self.model.item_type

        if bullet_points:
            self.view.show_bullet_point_list(item_type, items)
        else:
            self.view.show_number_point_list()

    def show_item(self, item_name):
        try:
            item = self.model.read_item(item_name)
            item_type = self.model.item_type
            self.view.show_item(item_type, item_name, item)
        except m_ex.ItemNotStored as e:
            self.view.display_missing_item_error(item_name, e)

    def insert_item(self, name, price, quantity):
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type

        try:
            self.model.create_item(name, price, quantity)
            self.view.display_item_stored(name, item_type)
        except m_ex.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(name, item_type, e)

    def update_item(self, name, price, quantity):
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type

        try:
            older = self.model.read_item(name)
            self.model.update_item(name, price, quantity)
            self.view.display_item_update(
                name, older['price'], older['quantity'], price, quantity)
        except m_ex.ItemAlreadyStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)
            # if the item is not yet stored and we performed an update,
            # we have 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

    def update_item_type(self, new_item_type):
        old_item_type = self.model.item_type
        self.model.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)

    def delete_item(self, name):
        item_type = self.model.item_type
        try:
            self.model.delete_item(name)
            self.view.display_item_deletion(name)
        except m_ex.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)
