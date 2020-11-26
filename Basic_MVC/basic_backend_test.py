from basic_backend import *


def main():
    my_items = [{'name': 'bread', 'price': 0.5, 'quantity': 20},
                {'name': 'milk', 'price': 1.0, 'quantity': 10},
                {'name': 'wine', 'price': 10.0, 'quantity': 5}, ]

    # ------
    # CREATE
    # ------
    create_items(my_items)
    create_item('beer', 3.0, 15)

    # if we try to recreate an object => ItemAlreadyStored exception:
    # create_item('beer', 2.0, 10)

    # ----
    # READ
    # ----
    print('READ items')
    print(read_items())

    # if we try to read an object not stored => ItemNotStored exception:
    # print('READ chocolate')
    # print(read_item('chocolate'))

    print('READ bread')
    print(read_item('bread'))

    # ------
    # UPDATE
    # ------
    print('UPDATE bread')
    update_item('bread', 2.0, 30)

    # if we try to update an object not stored => ItemNotStored exception
    # print('UPDATE chocolate')
    # update_item('chocolate', 10.0, 20)

    # ------
    # DELETE
    # ------
    print('DELETE beer')
    delete_item('beer')

    # if we try to delete an object not stored => ItemNotStored exception
    # print('DELETE chocolate')
    # delete_item('chocolate')

    print('READ items')
    print(read_items())


if __name__ == '__main__':
    main()
