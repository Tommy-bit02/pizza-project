
class Pizza():
    def __init__(self):
        self.toppings = []

    def is_veggetarian(self):
        # Default behavior for base class (assuming vegetarian by default)
        return all(topping != "sausage" for topping in self.toppings)

    def calculate_price(self):
        # Base price for pizza (add toppings later)
        return 8.0

    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)

# Subclass for Cheese (adds toppings to base pizza)
class Cheese(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.base = pizza

    def is_veggetarian(self):
        # Delegate to base pizza's is_veggetarian
        return self.base.is_veggetarian()

    def calculate_price(self):
        # Add price for cheese to base pizza price
        return 1.0 + self.base.calculate_price()

    def remove_topping(self, topping):
        # Remove topping from base pizza
        self.base.remove_topping(topping)

# Subclass for ThinCrust Pizza (defines specific crust)
class ThinCrust(Pizza):
    def __init__(self):
        super().__init__()
        self.crust = "thin"

    def is_veggetarian(self):
        # Thin crust pizza is vegetarian by default
        return True

    def calculate_price(self):
        # Price for thin crust pizza
        return 8.0

