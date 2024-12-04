# import hello_world

import csv

menu = [
    { 'item': 'Cappuccino', 'price': 4.50 },
    { 'item': 'English Breakfast Tea', 'price': 3.50 },
    { 'item': 'Blueberry Muffin', 'price': 5 }
]

with open('cafe_menu.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=menu[0].keys())
    writer.writeheader()
    writer.writerows(menu)


# with open('test.txt', 'r+') as f:
#     f.write("\nbean")

#     read = f.read(100)
#     position = f.tell()
#     print ("Current file position : ", position )
#     print(read)


# def show_shopping_list():
#     with open('shopping_list.txt', 'r') as f:
#         for item in f:
#             print(f'* {item.strip()}')


# if __name__ == '__main__':
#     show_shopping_list()

# hello_world.output()

