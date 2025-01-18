class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"{self.name} ({self.category}): ${self.price:.2f}"

class FoodItem(MenuItem):
    def __init__(self, name, price, calories):
        super().__init__(name, price, "food")
        self.calories = calories

    def get_info(self):
        return f"{super().get_info()}, Calories: {self.calories}"

class DrinkItem(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price, "drink")
        self.size = size

    def get_info(self):
        return f"{super().get_info()}, Size: {self.size}"

class Order:
    def __init__(self, order_id, currency="USD"):
        self.order_id = order_id
        self.items = []
        self.status = "pending"
        self.currency = currency
        self.exchange_rate = 36.57 if currency == "UAH" else 1.0  # Example rate for UAH to USD

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items) * self.exchange_rate

    def set_status(self, status):
        if status in ["pending", "preparing", "ready", "completed"]:
            self.status = status
        else:
            raise ValueError("Invalid status")

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print("Items:")
        for item in self.items:
            print(f"- {item.get_info()}")
        total = self.calculate_total()
        currency_symbol = "₴" if self.currency == "UAH" else "$"
        print(f"Total: {currency_symbol}{total:.2f}")
        print(f"Status: {self.status}")

        
pizza = FoodItem("Pizza", 8.99, 700)
burger = FoodItem("Burger", 5.49, 500)
coffee = DrinkItem("Coffee", 2.99, "M")
tea = DrinkItem("Tea", 1.99, "S")


currency = input("In which currency would you like the order to be displayed? (USD or UAH): ").strip().upper()
if currency not in ["USD", "UAH"]:
    print("Invalid currency. Defaulting to USD.")
    currency = "USD"


order1 = Order(order_id=1, currency=currency)
order2 = Order(order_id=2, currency=currency)

order1.add_item(pizza)
order1.add_item(coffee)

order2.add_item(burger)
order2.add_item(tea)

print("\nOrder 1:")
order1.display_order()

print("\nOrder 2:")
order2.display_order()


order1.set_status("preparing")
print("\nUpdated Order 1 Status:")
order1.display_order()

order2.set_status("ready")
print("\nUpdated Order 2 Status:")
order2.display_order()