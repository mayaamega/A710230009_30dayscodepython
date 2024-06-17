class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display_product(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock} units")
        print("------------------------")

    def update_stock(self, quantity):
        self.stock += quantity

class Cashier:
    def __init__(self):
        self.cart = []
        self.total_price = 0.0

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart.append((product, quantity))
            product.update_stock(-quantity)
            self.total_price += product.price * quantity
            print(f"{product.name} added to cart")
        else:
            print(f"Sorry, {product.name} is out of stock.")

    def remove_from_cart(self, product, quantity):
        for item in self.cart:
            if item[0] == product:
                self.cart.remove(item)
                product.update_stock(quantity)
                self.total_price -= product.price * quantity
                print(f"{quantity} unit(s) of {product.name} removed from cart")
                return
        print(f"{product.name} is not in the cart.")

    def checkout(self):
        if self.cart:
            print("--------- Receipt ---------")
            for item in self.cart:
                product, quantity = item
                print(f"{product.name} - ${product.price} x {quantity} = ${product.price * quantity}")
            print(f"Total: ${self.total_price}")
            print("---------------------------")
            self.cart = []
            self.total_price = 0.0
        else:
            print("Your cart is empty.")

# Contoh penggunaan:
# Membuat beberapa produk
product1 = Product(1, "Keyboard", 20.0, 10)
product2 = Product(2, "Mouse", 10.0, 15)
product3 = Product(3, "Monitor", 150.0, 5)

# Membuat objek kasir
cashier = Cashier()

# Menambahkan produk ke keranjang
cashier.add_to_cart(product1, 2)
cashier.add_to_cart(product2, 1)
cashier.add_to_cart(product3, 1)

# Menghapus produk dari keranjang
cashier.remove_from_cart(product1, 1)

# Checkout
cashier.checkout()

# Menampilkan produk
print("Updated Product Details:")
product1.display_product()
product2.display_product()
product3.display_product()
