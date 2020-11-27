import controller as co
from model import ModelBasic as mb
from view import View as v

my_items = [
    {'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'name': 'wine', 'price': 10.0, 'quantity': 5},
]

c = co.Controller(mb(my_items), v)

print('\nShow all items - with bullet points:')
c.show_items()

print('\nShow all items - no bullet points:')
c.show_items(bullet_points=True)

print("\nShow an non-existent item: chocolate")
c.show_item('chocolate')

print('\nShow an existent item: bread')
c.show_item('bread')

print('\nInsert and existing item: bread')
c.insert_item('brad', price=1.0, quantity=5)

print('\nInsert item not stored: chocolate')
c.insert_item('chocolate', price=2.0, quantity=10)

print('\nShow just inserted item: chocolate')
c.show_item('chocolate')

print('\nUpdate and existing item: milk')
c.update_item('milk', price=1.2, quantity=20)

print('\nUpdating an item that is not stored: ice cream')
c.update_item('ice cream', price=3.5, quantity=20)

print('\nDeleting an non-existing item: fish')
c.delete_item('fish')

print('\nDeleting an item that is available: bread')
c.delete_item('bread')
