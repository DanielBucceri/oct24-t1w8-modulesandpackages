# from color50 import rgb, constants

# # Define a color using RGB values
# my_color = rgb(128, 0, 128)  # Purple

# # Print colored text
# print(my_color + "Hello, World!")

# print("hellow world")

class Product:
    def __init__(self, name, price, stock):
        
        self.name = name
        self.price = price
        self.stock = stock
        
    def price(self):
        return self.price   
        
product = Product()
product.price = -100  # No validation here, could set an invalid value
