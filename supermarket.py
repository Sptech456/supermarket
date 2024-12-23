print("WELCOME TO FEWA SUPERMARKET")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity:
            product.quantity -= quantity
            self.cart.append((product, quantity))
        else:
            print(f" {product.name} {product.quantity} ")

    def generate_bill(self):
        total = 0
        print(f"Customer Bill for {self.name}:")
        for product, quantity in self.cart:
            item_total = product.price * quantity
            print(f"{quantity} x {product.name}: ${item_total:.2f}")
            total += item_total
        print(f"Total: ${total:.2f}")

class Supermarket:
    def __init__(self):
        self.products = {
            "Headphones": Product("Headphones", 800, 50),
            "Chocolate": Product("Chocolate", 100, 60),
            "Perfume": Product("Perfume", 500, 50),
            "Bread": Product("Bread", 60, 70),
            "Soap": Product("Soap", 50, 80),
            "Juice": Product("Juice", 200, 150)
        }
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def display_products(self):
        print("Available Products:")
        for product_name, product in self.products.items():
            print(f"- {product_name}: ${product.price:.2f} (Quantity: {product.quantity})")

    def add_to_cart(self, customer, product_name, quantity):
        product = self.products.get(product_name)
        if product:
            customer.add_to_cart(product, quantity)
        else:
            print(f"{product_name} ")

    def generate_receipt(self, customer):
        customer.generate_bill()

supermarket = Supermarket()
supermarket.display_products()

customer1 = Customer(name="Harish")
supermarket.add_customer(customer1)
supermarket.add_to_cart(customer1, "Headphones", 3)
supermarket.add_to_cart(customer1, "Chocolate", 5)
supermarket.add_to_cart(customer1, "Perfume", 1)

customer2 = Customer(name="Manish")
supermarket.add_customer(customer2)
supermarket.add_to_cart(customer2, "Bread", 2)
supermarket.add_to_cart(customer2, "Soap", 3)
supermarket.add_to_cart(customer2, "Juice", 2)

customer3 = Customer(name="Suman")
supermarket.add_customer(customer3)
supermarket.add_to_cart(customer3, "Perfume", 1)
supermarket.add_to_cart(customer3, "Chocolate", 2)

supermarket.generate_receipt(customer1)
supermarket.generate_receipt(customer2)
supermarket.generate_receipt(customer3)

print("\nThank you for your visit!")


            
            