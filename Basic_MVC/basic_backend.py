"""
here we implement the CRUD operations
"""


import mvc_exceptions as m_ex

items = []  # global variable where we keep the data.


def create_items(app_items):
    global items
    items = app_items


def create_item(name, price, quantity):
    global items
    result = list(filter(lambda x: x['name'] == name, items))
    if result:
        raise m_ex.ItemAlreadyStored(f'{name} already stored!')
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})


def read_item(name):
    global items
    my_items = list(filter(lambda x: x['name'] == name, items))
    if my_items:
        return my_items[0]
    else:
        raise m_ex.ItemNotStored(f'{name} not stored!')


def read_items():
    global items
    return items


def update_item(name, price, quantity):
    global items

    # since Python 3.x - no more tuple unpacking (PEP 3113) => we have to
    # do it manually (i_x = tuple, idxs_items = list(tuples))
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name,
                             enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise m_ex.ItemNotStored(f'Can\'t update {name}. Is not stored!')


def delete_item(name):
    global items

    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name,
                             enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise m_ex.ItemNotStored(f'Can\'t delete {name}. Is not stored!')
