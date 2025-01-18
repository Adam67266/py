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
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.status = "pending"

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

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
        print(f"Total: ${self.calculate_total():.2f}")
        print(f"Status: {self.status}")


pizza = FoodItem("Pizza", 8.99, 700)
burger = FoodItem("Burger", 5.49, 500)
coffee = DrinkItem("Coffee", 2.99, "M")
tea = DrinkItem("Tea", 1.99, "S")


order = Order(order_id=1)


order.add_item(pizza)
order.add_item(burger)
order.add_item(coffee)
order.add_item(tea)


order.display_order()


order.set_status("preparing")
print("\nUpdated Order Status:")
order.display_order()
