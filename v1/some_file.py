# Constants for crust types, toppings, and prices
crusts = {'thin', 'deepdish', 'hand_tossed'}
toppings = {'cheese', 'sausage', 'black_olive'}
meats = {'sausage'}

prices = {'thin': 8.0,
          'deepdish': 8.0,
          'hand_tossed': 8.0,
          'cheese': 1.0,
          'sausage': 1.5,
          'black_olive': 1.0}

# Function to make a pizza with a specific crust
def make_pizza(crust):
    if crust not in crusts:
        raise AttributeError('Invalid crust: ' + str(crust))
    return {'crust': crust, 'toppings': []}

# Function to get the crust of a pizza
def get_crust(pizza):
    return pizza['crust']

# Function to get the toppings of a pizza
def get_toppings(pizza):
    return pizza['toppings']

# Function to add a topping to a pizza
def add_topping(pizza, topping):
    if topping not in toppings:
        raise AttributeError('Invalid topping: ' + str(topping))
    pizza['toppings'].append(topping)

# Function to check if the pizza is vegetarian
def is_vegetarian(pizza):
    return not (meats & set(pizza['toppings']))

# Function to calculate the price of the pizza
def calculate_price(pizza):
    total = prices[pizza['crust']]  # Start with the price of the crust
    for topping in pizza['toppings']:
        total += prices[topping]  # Add the price of each topping
    return total

# Function to remove a topping from a pizza
def remove_topping(pizza, topping):
    if topping in pizza['toppings']:
        pizza['toppings'].remove(topping)
    else:
        raise AttributeError('Topping not found: ' + str(topping))

