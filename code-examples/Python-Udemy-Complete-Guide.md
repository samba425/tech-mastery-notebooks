# Python Udemy Course - Complete Guide

*Consolidated from python-udemy-main directory*

Generated on: Sat Dec 27 18:40:13 IST 2025

---

## Table of Contents

1. [00 Python](#00-python)
2. [02 Datatypes](#02-datatypes)
3. [03 Conditionals](#03-conditionals)
4. [04 Loops](#04-loops)
5. [05 Functions](#05-functions)
6. [06 Chai Business](#06-chai-business)
7. [07 Comprehensions](#07-comprehensions)
8. [08 Generators](#08-generators)
9. [09 Decorators](#09-decorators)
10. [10 Oop](#10-oop)
11. [11 Exceptions](#11-exceptions)
12. [12 Threads Concurrency](#12-threads-concurrency)
13. [13 Async Python](#13-async-python)
14. [14 Pydantic](#14-pydantic)
15. [Challenges](#challenges)

---

## 00 Python

*Section: 00_python*

### 00_python/non_python_code.py

**File:** `non_python_code.py`

```python
def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    add_to_cup("tea_leaves")
    add_to_cup("sugar")
    pour("boiled water")
    stie("cup")
    serve("chai")


make_chai()
```

---

### 00_python/non_python_shop.py

**File:** `non_python_shop.py`

```python
class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping chai")

    def add_sugar(self, amount):
        print("added the sugar")

my_chai = Chai(sweetness=3, milk_level=2)

my_chai.add_sugar(3)
```

---

## 02 Datatypes

*Section: 02_datatypes*

### 02_datatypes/chapter_1.py

**File:** `chapter_1.py`

```python
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")
```

---

### 02_datatypes/chapter_10.py

**File:** `chapter_10.py`

```python
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}")
```

---

### 02_datatypes/chapter_11.py

**File:** `chapter_11.py`

```python
import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])
```

---

### 02_datatypes/chapter_2.py

**File:** `chapter_2.py`

```python
spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")
print(f"Initial spice mix id: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")
```

---

### 02_datatypes/chapter_3.py

**File:** `chapter_3.py`

```python
# Interger

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaing_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaing_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_falvour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strenght {powerful_falvour}")
# 2 * 2 * 2

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")
```

---

### 02_datatypes/chapter_4.py

**File:** `chapter_4.py`

```python
is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")
```

---

### 02_datatypes/chapter_5.py

**File:** `chapter_5.py`

```python
import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }")
print(sys.float_info)
```

---

### 02_datatypes/chapter_6.py

**File:** `chapter_6.py`

```python
chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")

label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")
```

---

### 02_datatypes/chapter_7.py

**File:** `chapter_7.py`

```python
masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# membership testing

print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")
```

---

### 02_datatypes/chapter_8.py

**File:** `chapter_8.py`

```python
ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")
```

---

### 02_datatypes/chapter_9.py

**File:** `chapter_9.py`

```python
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")


```

---

## 03 Conditionals

*Section: 03_conditionals*

### 03_conditionals/chai_price_calculator.py

**File:** `chai_price_calculator.py`

```python
cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("Price is 15 rupees")
elif cup == "large":
    print("price is 20 rupees")
else:
    print("Unknown cup size")
```

---

### 03_conditionals/delivery_fees_waiver.py

**File:** `delivery_fees_waiver.py`

```python
order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is : {delivery_fees}")
```

---

### 03_conditionals/mini_story_1.py

**File:** `mini_story_1.py`

```python
kettle_boiled = False

if kettle_boiled:
    print("Kellle Done! time to make Chai")
```

---

### 03_conditionals/smart_thermostat.py

**File:** `smart_thermostat.py`

```python
device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")
```

---

### 03_conditionals/snak_suggestion.py

**File:** `snak_suggestion.py`

```python
snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")
```

---

### 03_conditionals/train_seat.py

**File:** `train_seat.py`

```python
seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()


match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")
```

---

## 04 Loops

*Section: 04_loops*

### 04_loops/01_token_dispneser.py

**File:** `01_token_dispneser.py`

```python
for token in range(1, 11):
    print(f"Serving chai to Token #{token}")
```

---

### 04_loops/02_batch_chai.py

**File:** `02_batch_chai.py`

```python
for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}")
```

---

### 04_loops/03_tea_orders.py

**File:** `03_tea_orders.py`

```python
orders = ["hitesh", "Aman", "Becky", "Carlos"]

for name in orders:
    print(f"Order ready for {name}")
```

---

### 04_loops/04_tea_menu.py

**File:** `04_tea_menu.py`

```python
menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")
```

---

### 04_loops/05_order_summary.py

**File:** `05_order_summary.py`

```python
names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
```

---

### 04_loops/06_tea-temperature.py

**File:** `06_tea-temperature.py`

```python
temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}")
    # temperature = temperature + 15
    temperature += 15

print("Tea is ready to boil")
```

---

### 04_loops/07_put_of_order.py

**File:** `07_put_of_order.py`

```python
flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]


for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")
    
print(f"Out side of loop")
```

---

### 04_loops/08_for_else.py

**File:** `08_for_else.py`

```python
staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")
```

---

### 04_loops/09_walrus.py

**File:** `09_walrus.py`

```python
# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


value = 13

if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")


# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")



flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")
```

---

### 04_loops/10_dictionary_case.py

**File:** `10_dictionary_case.py`

```python
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")
```

---

## 05 Functions

*Section: 05_functions*

### 05_functions/01_duplication.py

**File:** `01_duplication.py`

```python
def print_order(name, chai_type):
    print(f"{name} orderded {chai_type} chai!")


print_order("Aman", "masala")
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")


```

---

### 05_functions/02_complex.py

**File:** `02_complex.py`

```python
def fetch_sales():
    print("Fetching the sales data")


def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")


def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")


generate_report()
```

---

### 05_functions/03_hiding.py

**File:** `03_hiding.py`

```python
def get_input():
    print("Getting user input")

def validate_input():
    print("Validating the user info")

def save_to_db():
    print("saving to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete")


register_user()
```

---

### 05_functions/04_readability.py

**File:** `04_readability.py`

```python
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(3, 15)
print(my_bill)

print("Order for table 2: ", calculate_bill(2, 50))
```

---

### 05_functions/05_trace.py

**File:** `05_trace.py`

```python
def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")
```

---

### 05_functions/06_scopes.py

**File:** `06_scopes.py`

```python
def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_order)
    print_order()
    print("Outer: ", chai_order)

chai_order = "Tulsi" # Global
chai_counter()
print("Global :", chai_order)
```

---

### 05_functions/07_nonlocal.py

**File:** `07_nonlocal.py`

```python

chai_type = "ginger"
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()
```

---

### 05_functions/08_global_scope.py

**File:** `08_global_scope.py`

```python
chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
    kitchen()


front_desk()
print("Final global chai: ", chai_type)
```

---

### 05_functions/09_input_params.py

**File:** `09_input_params.py`

```python
# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing ", order)


# prepare_chai(chai)
# print(chai)


chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea="Green", sugar="Medium", milk="No") #keywords


def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()
```

---

### 05_functions/10_return.py

**File:** `10_return.py`

```python
# def make_chai():
#     # return "Here is your masal chai"
#     print("Here is your masala chai")

# return_value = make_chai()

# print(return_value)

def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"
    print("chai")

print(chai_status(0))
print(chai_status(5))


def chai_report():
    return 100, 20, 10 # sold, remaining

sold, remaining, not_paid = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)
```

---

### 05_functions/11_types_of_functions.py

**File:** `11_types_of_functions.py`

```python
def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups


def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))



chai_types = ["light", "kadak", "ginger", "kadak"]


strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai)
```

---

### 05_functions/12_built_in.py

**File:** `12_built_in.py`

```python
def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    chai="ginger"
    return flavor


print(chai_flavor.__doc__)
print(chai_flavor.__name__)

help(len)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: NUmber of samosa (15 rupees each)
    : return: (total amount, thank you message as string)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"
```

---

## 06 Chai Business

*Section: 06_chai_business*

### 06_chai_business/main.py

**File:** `main.py`

```python
# import recipes.flavors

# print(recipes.flavors.ginger_chai())


# from recipes.flavors import elachai_chai, ginger_chai

# print(ginger_chai())


```

---

### 06_chai_business/recipes/__init__.py

**File:** `__init__.py`

```python

```

---

### 06_chai_business/recipes/flavors.py

**File:** `flavors.py`

```python
def elachai_chai():
    return "Elachai chai is ready"

def ginger_chai():
    return "Ginger chai is ready"
```

---

### 06_chai_business/utils/discounts.py

**File:** `discounts.py`

```python

```

---

## 07 Comprehensions

*Section: 07_comprehensions*

### 07_comprehensions/01_list_compre.py

**File:** `01_list_compre.py`

```python
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea)
```

---

### 07_comprehensions/02_set_compre.py

**File:** `02_set_compre.py`

```python
favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais }
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)
```

---

### 07_comprehensions/03_dict_compre.py

**File:** `03_dict_compre.py`

```python
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
```

---

### 07_comprehensions/04_genrator_compre.py

**File:** `04_genrator_compre.py`

```python
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)
```

---

## 08 Generators

*Section: 08_generators*

### 08_generators/01_basics.py

**File:** `01_basics.py`

```python
def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) # gives error
```

---

### 08_generators/02_infinite_generators.py

**File:** `02_infinite_generators.py`

```python
def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))
```

---

### 08_generators/03_send_generators.py

**File:** `03_send_generators.py`

```python
def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala Chai")
stall.send("Lemon Chai")
```

---

### 08_generators/04_close_generator.py

**File:** `04_close_generator.py`

```python
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")


stall = chai_stall()
print(next(stall))
stall.close() #cleanup
```

---

## 09 Decorators

*Section: 09_decorators*

### 09_decorators/01_basics.py

**File:** `01_basics.py`

```python
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chaicode")


greet()
print(greet.__name__)
```

---

### 09_decorators/02_logging_decorator.py

**File:** `02_logging_decorator.py`

```python
from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")

brew_chai("Masala")
```

---

### 09_decorators/03_auth_decorator.py

**File:** `03_auth_decorator.py`

```python
from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def acess_tea_inventory(role):
    print("Access granted to tea inventory")

acess_tea_inventory("user")
acess_tea_inventory("admin")
```

---

## 10 Oop

*Section: 10_oop*

### 10_oop/01_simple_class.py

**File:** `01_simple_class.py`

```python
class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai()
print(type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
```

---

### 10_oop/02_namespace.py

**File:** `02_namespace.py`

```python
class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# creating objects from class Chai

masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")
masala.is_hot = False

print("Class: ", Chai.is_hot)
print(f"Masala {masala.is_hot}")
masala.flavor = "Masala"
print(masala.flavor)
```

---

### 10_oop/03_attribute_shadowing.py

**File:** `03_attribute_shadowing.py`

```python
class Chai:
    temperature = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ",cutting.temperature)
print("cup size is  ",cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup)
```

---

### 10_oop/04_self_args.py

**File:** `04_self_args.py`

```python
class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))
```

---

### 10_oop/05_init_objects.py

**File:** `05_init_objects.py`

```python
class ChaiOrder:
    
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())
```

---

### 10_oop/06_inheritance_composition.py

**File:** `06_inheritance_composition.py`

```python
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()
```

---

### 10_oop/07_base_class.py

**File:** `07_base_class.py`

```python
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level
        

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
```

---

### 10_oop/08_mro.py

**File:** `08_mro.py`

```python
class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(C, B):
    pass

cup = D()
print(cup.label)
print(D.__mro__)
```

---

### 10_oop/09_static_methods.py

**File:** `09_static_methods.py`

```python
class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = " water , milk , ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
```

---

### 10_oop/10_classmethod.py

**File:** `10_classmethod.py`

```python
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(ChaiUtils.is_valid_size("Medium"))

order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})

order2 = ChaiOrder.from_string("Ginger-Low-Small")

order3 = ChaiOrder("Large", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
```

---

### 10_oop/11_propert_decorators.py

**File:** `11_propert_decorators.py`

```python
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 6
print(leaf.age)

```

---

## 11 Exceptions

*Section: 11_exceptions*

### 11_exceptions/01_basic.py

**File:** `01_basic.py`

```python
orders = ["masala", "ginger"]

print(orders[2])
```

---

### 11_exceptions/02_try_except.py

**File:** `02_try_except.py`

```python
chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are tying to access does not exists")


print("Hello chai code")
```

---

### 11_exceptions/03_complex_try.py

**File:** `03_complex_try.py`

```python
def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")

serve_chai("masala")
serve_chai("unknown")
```

---

### 11_exceptions/04_multiple_exception.py

**File:** `04_multiple_exception.py`

```python
def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2)
process_order("masala", "two")
```

---

### 11_exceptions/05_custom_exceptions.py

**File:** `05_custom_exceptions.py`

```python
def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")


brew_chai("mint")
```

---

### 11_exceptions/06_custom_except_two.py

**File:** `06_custom_except_two.py`

```python
class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("chai is ready...")


make_chai(0, 1)
```

---

### 11_exceptions/07_complete_order.py

**File:** `07_complete_order.py`

```python
class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting chaicode!")


bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)
```

---

### 11_exceptions/08_file_handling.py

**File:** `08_file_handling.py`

```python
# file = open("order.txt", "w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()


with open("order.txt", "w") as file:
    file.write("ginger tea - 4 cups")
```

---

## 12 Threads Concurrency

*Section: 12_threads_concurrency*

### 12_threads_concurrency/01_threading.py

**File:** `01_threading.py`

```python
import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)
        
# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")
```

---

### 12_threads_concurrency/02_multiprocessing.py

**File:** `02_multiprocessing.py`

```python
from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(3)
    ]

    # Start all process
    for p in chai_makers:
        p.start()

    # wait for all to complete
    for p in chai_makers:
        p.join()

    print("All chai served")
```

---

### 12_threads_concurrency/03_gil_threading.py

**File:** `03_gil_threading.py`

```python
import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

thread1 =threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken: {end - start:.2f} seconds")
```

---

### 12_threads_concurrency/04_gil_multiprocessing.py

**File:** `04_gil_multiprocessing.py`

```python
from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_number)
    p2= Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi-processing is {end - start:.2f} seconds")

```

---

### 12_threads_concurrency/05_thread_one.py

**File:** `05_thread_one.py`

```python
import threading
import time

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk Boiled...")

def toast_bun():
    print(f"Toasting bun...")
    time.sleep(3)
    print(f"Done with bun toast...")
    
start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Breakfast is ready in {end - start:.2f} seconds")
```

---

### 12_threads_concurrency/06_thread_two.py

**File:** `06_thread_two.py`

```python
import threading
import time

def prepare_chai(type_, wait_time ):
    print(f"{type_} chai: brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: Ready.")


t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 3))

t1.start()
t2.start()
t1.join()
t2.join()



```

---

### 12_threads_concurrency/07_thread_download.py

**File:** `07_thread_download.py`

```python
import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"All downloads done in {end - start:.2f} seconds")
```

---

### 12_threads_concurrency/08_thread_lock.py

**File:** `08_thread_lock.py`

```python
import threading

counter = 0
lock = threading.Lock()

def increament():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increament) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")
```

---

### 12_threads_concurrency/09_process_one.py

**File:** `09_process_one.py`

```python
import threading
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**7):
        total += i
    print("DONE ✅")

start = time.time()
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Time taken: {time.time() - start:.2f} seconds")
```

---

### 12_threads_concurrency/10_process_two.py

**File:** `10_process_two.py`

```python
from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**9):
        total += i
    print("DONE ✅")

if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f"Time taken: {time.time() - start:.2f} seconds")
```

---

### 12_threads_concurrency/11_process_queue.py

**File:** `11_process_queue.py`

```python
from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala chai is ready")



if __name__ == '__main__':
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get())
```

---

### 12_threads_concurrency/12_process_value.py

**File:** `12_process_value.py`

```python
from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value('i', 0)
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value: ",counter.value )
```

---

## 13 Async Python

*Section: 13_async_python*

### 13_async_python/01_async_one.py

**File:** `01_async_one.py`

```python
import asyncio

async def brew_chai():
    print("Brwing chai...")
    await asyncio.sleep(2)
    print("Chai is ready")

asyncio.run(brew_chai())
```

---

### 13_async_python/02_async_two.py

**File:** `02_async_two.py`

```python
import asyncio
import time
async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(3)
    # time.sleep(3)
    print(f" {name} is ready...")


async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Ginger chai"),
    )

asyncio.run(main())
```

---

### 13_async_python/03_async_three.py

**File:** `03_async_three.py`

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        # tasks = [t1, t2, t3]
        await asyncio.gather(*tasks)
        

asyncio.run(main())
```

---

### 13_async_python/04_thread_async.py

**File:** `04_thread_async.py`

```python
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala chai")
        print(result)

asyncio.run(main())
```

---

### 13_async_python/05_process_async.py

**File:** `05_process_async.py`

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"🔒 {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, "credit_card_1234")
        print(f"{result}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

### 13_async_python/06_bgworker.py

**File:** `06_bgworker.py`

```python
import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health 🕰️")

async def fetch_orders():
    await asyncio.sleep(3)
    print("🎁 order fetched")


threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_orders())
```

---

### 13_async_python/07_daemon.py

**File:** `07_daemon.py`

```python
import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done")
```

---

### 13_async_python/08_non_daemon.py

**File:** `08_non_daemon.py`

```python
import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done")
```

---

### 13_async_python/09_race_condition.py

**File:** `09_race_condition.py`

```python
import threading

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [ threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print("Chai stock: ", chai_stock)
```

---

### 13_async_python/10_deadlock.py

**File:** `10_deadlock.py`

```python
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    with lock_a:
        print("Task 1 acquired lock a")
        with lock_b:
            print("Task 1 acquired lock b")

def task2():
    with lock_b:
        print("Task 2 acquired lock b")
        with lock_a:
            print("Task 2 acquired lock a")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
```

---

## 14 Pydantic

*Section: 14_pydantic*

### 14_pydantic/01_basics/advance_nested_model.py

**File:** `advance_nested_model.py`

```python
from pydantic import BaseModel
from typing import Optional, List, Union


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None


class TextConent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextConent, ImageContent]]


class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address]=[]
```

---

### 14_pydantic/01_basics/advance_validators.py

**File:** `advance_validators.py`

```python
from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name : str

    @field_validator('first_name', 'last_name')
    def names_must_be_capitalize(cls, v):
        if not v.istitle():
            raise ValueError('Names must be capitilized')
        return v
    

class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()
    


class Product(BaseModel):
    price: str # $4.44

    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v
    
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime


    @model_validator(mode="after")
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('end_date must be after start_date')
        return values
```

---

### 14_pydantic/01_basics/computed_property.py

**File:** `computed_property.py`

```python
from pydantic import BaseModel, computed_field, Field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    
booking = Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=100.0
)

print(booking.total_amount)
print(booking.model_dump())
```

---

### 14_pydantic/01_basics/employee_model.py

**File:** `employee_model.py`

```python
from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Hitesh Choudhary"
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000
    )


class User(BaseModel):
    email: str = Field(...,regex=r'')
    phone: str = Field(..., regex=r'')
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )

```

---

### 14_pydantic/01_basics/field_example.py

**File:** `field_example.py`

```python
from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"laptop": 1, "mouse": 2, "keyboard": 3}
}

cart = Cart(**cart_data)
```

---

### 14_pydantic/01_basics/field_validation.py

**File:** `field_validation.py`

```python
from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v
    

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values
```

---

### 14_pydantic/01_basics/first_model.py

**File:** `first_model.py`

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': '101a', 'name': "Chaicode", 'is_active': True}

user = User(**input_data)
print(user)
```

---

### 14_pydantic/01_basics/nested_model.py

**File:** `nested_model.py`

```python
from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street="123 something",
    city="Jaipur",
    postal_code="100001"
)

user = User(
    id=1,
    name="Hitesh",
    address=address,
)


user_data = {
    "id": 1,
    "name": "Hitesh",
    "address": {
        "street": "321 something",
        "city": "Paris",
        "postal_code": "20002"
    }
}

user = User(**user_data)
print(user)
```

---

### 14_pydantic/01_basics/product_model.py

**File:** `product_model.py`

```python
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name="Laptop", price=999.99, in_stock=True)

product_two = Product(id=2, name="Mouse", price=24.33)

product_three = Product(name="keyboard")
```

---

### 14_pydantic/01_basics/self_reference.py

**File:** `self_reference.py`

```python
from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()


comment = Comment(
    id= 1,
    content="First comment",
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(id=3, content="reply 2", replies=[
            Comment(id=4, content="nested reply")
        ])
    ]
)
```

---

### 14_pydantic/02_serialization/serial.py

**File:** `serial.py`

```python
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name="Hitesh",
    email="h@hitesh.ai",
    createdAt=datetime(2024, 3, 15, 14, 30,),
    address=Address(
        street="Something",
        city="Jaipur",
        zip_code="009988"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)

json_str = user.model_dump_json()
print("="*30)
print(json_str)
```

---

## Challenges

*Section: challenges*

### challenges/01_utilities/day_1.py

**File:** `day_1.py`

```python
"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""
import datetime

name = input("What is your name ? ").strip()
age = input("How old are you ? ").strip()
city = input("Which city do you live in? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("WHat is your favourite hobby? ").strip()

intro_message = (
    f"Hello! my name is {name}, I'm {age} years old and live in {city}. "
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
    f"Nice to meet you!\n"
)


current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"


border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)
```

---

### challenges/01_utilities/day_10.py

**File:** `day_10.py`

```python
"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""
def encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(message, key):
    return encrypt(message, -key)


print("Secret message program")
choice = input("Do you want to E or D").strip().lower()

if choice == "e":
    text = input("Enter your message: \n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        encrypted = encrypt(text, key)
        print("Encrypted message: ")
        print(encrypted)
    except ValueError:
        print("Invalid key")
elif choice == 'd':
    text = input("Enter your encrypted message: \n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        decrypted = decrypt(text, key)
        print("Decrypted message: ")
        print(decrypted)
    except ValueError:
        print("Invalid key")
else:
    print("Invalid choice")
```

---

### challenges/01_utilities/day_11.py

**File:** `day_11.py`

```python
"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    
    return min(score, 100)

def run_friendship_calculator():
    print("❤️ Friendship Compatibility calculator ❤️")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    score = friendship_score(name1, name2)

    print(f"\n {score}")


run_friendship_calculator()
```

---

### challenges/01_utilities/day_2.py

**File:** `day_2.py`

```python
"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

import textwrap
name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favourite emoji: ").strip()
website = input("Enter your website: ").strip()

print("\nChoose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("Enter 1, 2 or 3: ").strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n💡 {passion}\n {website}" 
    elif style == "2":
        return f"{emoji} {name}\n {profession}🔥\n {passion} \n {website}🔥"
    elif style == "3":
        return f"{emoji*3}\n {name} - {profession}\n {passion}\n {website} \n {emoji*3}"
    
bio = generate_bio(style)

print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save this bio to a text file? (y/n): ").lower()

if save == 'y':
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("file saved")
```

---

### challenges/01_utilities/day_3.py

**File:** `day_3.py`

```python
"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number. ")

num_people = int(input("How many people are there in the group? "))
names = []

for i in range(num_people):
    name = input(f"Enter the name of persion #{i+1}").strip()
    names.append(name)

total_bill = get_float("Enter the bill amount in number only")

share = round(total_bill / num_people, 2)

print("\n" + "*" * 40)
print(f"Total bill: {total_bill}")
print(f"Each person owes {share}")

for name in names:
    print(f"{name} owes {share} rupees")

print("\n" + "*" * 40)
```

---

### challenges/01_utilities/day_4.py

**File:** `day_4.py`

```python
"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""


def calculate_minutes(age_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR

    return round(total_days), round(total_hours), round(total_minutes)


while True:
    try:
        age = float(input("Enter your age in years: "))
        days, hours, minutes = calculate_minutes(age)

        print("\n You are approx:")
        print(f"  -  {days} days old")
        print(f"  -  {hours} hours old")
        print(f"  -  {minutes} minutes old\n")

        again = input("Would you like to try again? (y/n)").strip().lower()

        if again != 'y':
            print("Good bye!")
            break
    except:
        print("Please enter a valid number for age")
```

---

### challenges/01_utilities/day_5.py

**File:** `day_5.py`

```python
"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""
# get a dictionary
emoji_map_fun = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}

# get user message
message = input("Enter your message: ")

updated_words = []
# process each word
for word in message.split():
    cleaned = word.lower().strip(".,!?")
    emoji = emoji_map_fun.get(cleaned, "")
    if emoji:
        updated_words.append(f"{word} {emoji}")
    else:
        updated_words.append(word)

updated_message = " ".join(updated_words)
print("\n Enhanced message:\n")
print(updated_message)
```

---

### challenges/01_utilities/day_6.py

**File:** `day_6.py`

```python
"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

import datetime

entry = input("What did you learn today ? ").strip()
rating = input("⭐️ rate your productivity today (1-5, optional)").strip()

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = f"\n 🗓️ {date_str}\n{entry}"
if rating:
    journal_entry += f"\n Productivity Rating: {rating}\n"
journal_entry += "\n" + "-" * 50

with open("learning_journal.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print(f"\n your journal entry has been saved to 'learning_journal.txt' file. ")

```

---

### challenges/01_utilities/day_7.py

**File:** `day_7.py`

```python
"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']}||{status}\n")


def display_tasks(tasks):
    if not tasks:
        print(f"NO tasks found")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()



def task_manager():
    tasks = load_tasks()

    while True:
        print("\n------Task List Manager -------")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5)").strip()

        match choice:
            case "1":
                text = input("Enter your task").strip()
                if text:
                    tasks.append({"text":text, "done": False})
                    save_tasks(tasks)
                else:
                    print("Task cannot be empty")

            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number"))
                    if 1 <= num <= len(tasks):
                        tasks[num-1]["done"] = True
                        save_tasks(tasks)
                        print("task marked as DONE")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "4":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete"))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        save_tasks(tasks)
                        print(f"task removed {removed['text']}")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "5":
                print("Exiting task Manager")
                break
            case _:
                print("Please choose a valid option")

task_manager()
```

---

### challenges/01_utilities/day_8.py

**File:** `day_8.py`

```python
"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import string
import random
import getpass

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Too short (minimum 8 characters)")
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter")
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter")
    if not any(c.isdigit() for c in password):
        issues.append("Missing a digit")
    if not any(c in string.punctuation  for c in password):
        issues.append("Missing a special character")
    return issues
    

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    
    return "".join(random.choice(chars) for _ in range(length))

password = getpass.getpass("Enter a password: ")
issues = check_password_strength(password)

if not issues:
    print("Strong password! you are good to go")
else:
    print("You got weak password")
    for issue in issues:
        print(f"- {issue}")

suggestion = generate_strong_password()
print("\n suggesting you a strong password")
print(suggestion)      
```

---

### challenges/01_utilities/day_9.py

**File:** `day_9.py`

```python
"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time

while True:
    try:
        seconds = int(input("⏰ Enter the time in seconds: "))
        if seconds < 1:
            print("Please enter a number greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input, please enter a whole number")


print("\n 🔔 Timer started...")
for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"🕰️ Time left: {time_format} ", end="\r")
    time.sleep(1)

print("\n Time's up! Take a break or move on to next task.")
#print("\a") # optional; makes a beep sound
```

---

### challenges/02_data_handling/day_1.py

**File:** `day_1.py`

```python
"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    #check for duplicates
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
           if row["Name"].lower() == name.lower():
               print("Contact name already exists")
               return
    
    with open(FILENAME, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added")


def view_contacts():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 1:
            print("No contacts found")
            return
        
        print("\n Your contacts: \n")

        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row["Name"]} | 📞 {row["Phone"]}")
                found = True

    if not found:
        print("No matching contact found")



def main():

    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4)").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thanks for using our software")
            break
        else:
            print("Invalid choice of number")


if __name__ == "__main__":
    main()

```

---

### challenges/02_data_handling/day_10.py

**File:** `day_10.py`

```python
"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
"""

import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    
    return Fernet(key)

fernet = load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save_vault(data):
    with open(VAULT_FILE, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({
        "title": title,
        "content": encrypted_content,
        "timestamp": timestamp
    })

    save_vault(data)
    print("✅ data saved")

def list_notes():
    data = load_vault()
    if not data:
        print("No notes yet")
        return
    
    for i, note in enumerate(data, 1):
        print(f"{i}. {note['title']} {note['timestamp']}")


def view_note():
    list_notes()
    try:
        index = int(input("Enter note number to view: ")) - 1
        data = load_vault()
        if 0 <= index <= len(data):
            encrypted = data[index]["content"]
            decrypted = fernet.decrypt(encrypted.encode()).decode()
            print(f"\n 📝 {data[index]['title']} - {data[index]['timestamp']} \n\n {decrypted}")
        else:
            print("Invalid selection")
    except:
        print("Invalid input")

def search_notes():
    keyword = input("Enter the keyword to search: ").strip().lower()
    data = load_vault()
    found = [note for note in data if keyword in note["title"].lower()]
    if not found:
        print("NO matching notes")
    else:
        for note in found:
            print(f"{note["title"]} {note['timestamp']}")

def main():
    while True:
        print("\n🔐 Offline Notes Locker")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Enter an option: ").strip()

        match choice:
            case "1": add_note()
            case "2": list_notes()
            case "3": view_note()
            case "4": search_notes()
            case "5": break
            case _: print("Invalid input")

if __name__ == "__main__":
    main()
```

---

### challenges/02_data_handling/day_2.py

**File:** `day_2.py`

```python
"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_student_data():
    students = {}

    while True:
        name = input("Enter the student name or done to exit: ").strip()
        
        if name.lower() == "done":
            break
        if name in students:
            print("Student already exists")
            continue

        try:
            marks = float(input(f"Enter marks for {name}: "))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks")

    return students


def display_report(students):
    if not students:
        print("No student data ❌")
        return
    
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks) / len(marks)

    topper = [name for name, score in students.items() if score == max_score ]
    bottomer = [name for name, score in students.items() if score == min_score ]

    print("\n Students marks report 🗓️")
    print("-" * 30)
    print(f"Total students: {len(students)}")
    print(f"average marks for students: {average:.2f}")
    print(f"Highest marks : {max_score} by {', '.join(topper)}")
    print(f"lowest marks : {min_score} by {', '.join(bottomer)}")

    print("-" * 30)
    print("Detailed Marks 🗓️")
    for name, score in students.items():
        print(f" - {name}: {score}")


students = collect_student_data()
display_report(students)
```

---

### challenges/02_data_handling/day_3.py

**File:** `day_3.py`

```python
"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import os
import json

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)


def add_movies(movies):
    title = input("Enter the movie name: ").strip().lower()

    if any(movie["title"].lower() == title for movie in movies):
        print("Movie already exists")
        return
    genre = input("Genre: ").strip().lower()
    try:
        rating = float(input("Enter rating(0-10): "))
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Please enter valid number")
        return
    
    movies.append({"title": title, "genre": genre, "rating": rating})
    save_movies(movies)
    print("Movie added ✅")
    
    
def search_movies(movies):
    term = input("Enter the title or genre: ").strip().lower()

    results = [
        movie for movie in movies 
        if term in movie['title'].lower() or term in movie['genre'].lower()
     
    ]
    if not results:
        print("No matching result")
        return
    print(f" Found {len(results)} result(s)")

    for movie in results:
        print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")


def view_movies(movies):
    if not movies:
        print("NO movies in DB")
        return
    print("-"*30)
    for movie in movies:
        print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")
    print("-"*30)



def run_movie_db():
    movies = load_movies()

    while True:
        print("\n🍿 MyMovieDB")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Exit")
    
        choice = input("Choose an option (1-4): ").strip()
        match choice:
            case "1": add_movies(movies)
            case "2": view_movies(movies)
            case "3": search_movies(movies)
            case "4": break
            case _: print("Enter valid choice") 


if __name__ == "__main__":
    run_movie_db()
```

---

### challenges/02_data_handling/day_4.py

**File:** `day_4.py`

```python
"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import os
import csv
from datetime import datetime
import requests

FILENAME = "weather_logs.csv"
API_KEY = "Get Your own key here" 
# keys are usually hidden in .env file but that is for later

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])

def log_weather():
   city = input("Enter your city name: ").strip()
   date = datetime.now().strftime("%Y-%m-%d")

   with open(FILENAME, "r", newline='', encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
          if row["Date"] == date and row['City'].lower() == city.lower():
              print("Entry for this city and date exists")
              return
          
   try:
       url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
       response = requests.get(url)
       data = response.json()

       if response.status_code != 200:
           print(f"API Error ")
           return
       temp = data["main"]["temp"]
       condition = data["weather"][0]["main"]

       with open(FILENAME, "a", newline='', encoding="utf-8") as f:
           writer = csv.writer(f)
           writer.writerow([date, city.title(), temp, condition])
           print(f"Logged: {temp} {condition} in {city.title()} on {date}")
   except Exception as e:
       print("Failed to make API call")


def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if len(reader) <=1:
            print("No Entries")
            return
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")


def main():
    while True:
        print("Real time weather logger")
        print("1. Add weather log")
        print("2. View weather log")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1": log_weather()
            case "2": view_logs()
            case _: print("Invalid choice")


if __name__ == "__main__":
    main()
```

---

### challenges/02_data_handling/day_5.py

**File:** `day_5.py`

```python
"""
Sample data:
Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Plot graphs from this data


"""
import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = "weather_logs.csv"
def visualize_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row["Date"])
                temps.append(row["Temperature"])
                conditions[row["Condition"]] += 1
            except:
                continue
    if not dates:
        print("NO data is available")
        return
    
    plt.figure(figsize=(10, 7))
    plt.plot(dates, temps, marker='o')
    plt.title("Temperature over time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.bar(conditions.keys(), conditions.values(), color='skyblue')
    plt.xlabel("Condition")
    plt.ylabel("Days")
    plt.show()



visualize_weather()
```

---

### challenges/02_data_handling/day_6.py

**File:** `day_6.py`

```python
"""
 Challenge: JSON-to-CSV Converter Tool

Create a Python utility that reads structured data (like you'd get from an API) from a `.json` file and converts it to a CSV file that can be opened in Excel.

Your program should:
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Bonus:
- Provide feedback on how many records were converted
- Allow user to define which fields to extract
- Handle missing fields gracefully
"""
import json
import csv
import os

INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"

def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    
    with open(filename, 'r', encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON format")

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return
    
    fieldname = list(data[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        for record in data:
            writer.writerow(record)
    
    print(f"Converted {len(data)} records to {output_file}")


def main():
    print("Converting JSON to CSV....")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
```

---

### challenges/02_data_handling/day_7.py

**File:** `day_7.py`

```python
"""
 Challenge: CSV-TO-JSON Converter Tool

"""

import os
import json
import csv

INPUT_FILE = "raw_data.csv"
OUTPUT_FILE = "converted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print("CSV file not found")
        return []
    
    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print(data)
        return data
    
def save_as_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Converted {len(data)} records to {filename}")

def preview_data(data, count=3):
    for row in data[:count]:
        print(json.dumps(row, indent=2))
    print(".......")


def main():

    data = load_csv_data(INPUT_FILE)
    if not data:
        return
    save_as_json(data, OUTPUT_FILE)
    preview_data(data)

if __name__ == "__main__":
    main()

```

---

### challenges/02_data_handling/day_8.py

**File:** `day_8.py`

```python
"""
Challenge : JSON Flattener

{
  "user": {
    "id": 1,
    "name": "Riya",
    "email": "riya@example.com",
    "address": {
      "city": "Delhi",
      "pincode": 110001
    }
  },
  "roles": ["admin", "editor"],
  "is_active": true
}

Flatten this to:

{
  "user.id": 1,
  "user.name": "Riya",
  "user.email": "riya@example.com",
  "user.address.city": "Delhi",
  "user.address.pincode": 110001,
  "roles.0": "admin",
  "roles.1": "editor",
  "is_active": true
}


"""

import json
import os

INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flattened_data.json"

def flatten_json(data, parent_key='', sep='.'):
    items = {}

    if isinstance(data, dict):
        for k, v in data.items():
            full_key = f"{parent_key}{sep}{k}" if parent_key else k
            print(full_key)
            items.update(flatten_json(v, full_key, sep=sep))

    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key =f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.update(flatten_json(item, full_key, sep=sep))
    else:
        items[parent_key] = data

    return items

def main():
    if not os.path.exists(INPUT_FILE):
        print("No input file found")
        return
    
    try:
        with open(INPUT_FILE, 'r', encoding="utf-8") as f:
            data = json.load(f)

        sep = input("Enter your seperator like . or -: ").strip() or '.'

        flattened = flatten_json(data, sep=sep)
        with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
            json.dump(flattened, f, indent=2)

        print(f"Flattened JSON saved to {OUTPUT_FILE}")
    except Exception as e:
        print("Failed to faltten the data", e)

if __name__ == "__main__":
    main()
```

---

### challenges/02_data_handling/day_9.py

**File:** `day_9.py`

```python
"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64
import os

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*().,<>" for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special])
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]


def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = password_strength(password)

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding="utf-8") as f:
        f.write(encoded_line + "\n")

    print("✅ Credential saved")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return
    
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            hidden_password = '*' * len(password)
            print(f"{website} | {username} | {password}")


def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1": add_credential()
            case "2": view_credentials()
            case "4": break
            case _: print("Invalid choice")

if __name__ == "__main__":
    main()
```

---

### challenges/03_web_scraping/day_01.py

**File:** `day_01.py`

```python
"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_h2_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    print(h2_tags)
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)
    print(headers)

get_h2_headers(URL)
```

---

### challenges/03_web_scraping/day_02.py

**File:** `day_02.py`

```python
"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""
import csv
import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_top20.csv"


def fetch_top_post():
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Network error \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")
    # print(post_links)

    posts = []
    for link in post_links[:20]:
        title = link.text.strip()
        url = link.get("href").strip()
        # print(f"{title} \n {url} \n\n")
        posts.append({"title": title, "url": url})

    return posts


def save_to_csv(posts):
    if not posts:
        print("Noting to save")
        return
    
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url"])
        writer.writeheader()
        writer.writerows(posts)

    print(f"✅ Saved Hacker News to {CSV_FILE}")



def main():
    print("Scrapping the HN portal....")
    posts = fetch_top_post()      
    print("Collected all data...")
    save_to_csv(posts)

if __name__ == "__main__":
    main()


```

---

### challenges/03_web_scraping/day_03.py

**File:** `day_03.py`

```python
"""
 Challenge: Scrape Books To Scrape (70 Books)

Goal:
- Visit https://books.toscrape.com/
- Scrape each book's:
  • Title 
  • Price 

You must:
- Crawl through multiple pages using the "next" button until you collect 70 books.
- Save the data to a JSON file: books_data.json
- Handle network errors gracefully.

Bonus:
- Track how many books scraped
- Print progress as you collect pages
"""


import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
START_PAGE = "catalogue/page-1.html"
OUTPUT_PAGE = "books_data.json"
TARGET_COUNT = 70

def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Failed to fetch url")
        return [], None
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price = article.select_one("p.price_color").text.strip()
        # print(f"{title} - {price}")
        books.append({"title":title, "price":price})

    next_link = soup.select_one("li.next > a")
    next_url = urljoin(url, next_link.get("href")) if next_link else None

    return books, next_url


def main():
    collected = []
    current_url = urljoin(BASE_URL, START_PAGE)

    while len(collected) < TARGET_COUNT and current_url:
        print(f"Scrapping: {current_url}")
        books, next_url = scrape_page(current_url)
        collected.extend(books)
        current_url = next_url

    collected = collected[:TARGET_COUNT]
    print(f"scrapped {len(collected)} books")

    with open(OUTPUT_PAGE, "w", encoding="utf-8") as f:
        json.dump(collected, f, indent=2)

    print(f"Data save to {OUTPUT_PAGE}")


if __name__ == "__main__":
    main()

```

---

### challenges/03_web_scraping/day_04.py

**File:** `day_04.py`

```python
"""
 Challenge: Download Cover Images of First 10 Books

Goal:
- Visit https://books.toscrape.com/
- Scrape the first 10 books listed on the homepage
- For each book, extract:
  • Title
  • Image URL

Then:
- Download each image
- Save it to a local `images/` folder with the filename as the book title (sanitized)

Example:
 Title: "A Light in the Attic"
 Saved as: images/A_Light_in_the_Attic.jpg

Bonus:
- Handle invalid filename characters
- Show download progress
"""
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

def download_image(img_url, filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} - {e}")


def scrape_and_download_images():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    for book in books:
        title = book.h3.a['title']
        relative_img = book.find("img")["src"]
        img_url = urljoin(BASE_URL, relative_img)
        print(f"url - {img_url}")

        filename = sanitize_filename(title) + ".jpg"
        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"filepath - {filepath}")

        print(f"Downloading: {title}")
        download_image(img_url, filepath)
    print("All 10 books covers downloaded to images/")

if __name__ == "__main__":
    scrape_and_download_images()
```

---

### challenges/03_web_scraping/day_05.py

**File:** `day_05.py`

```python
"""
 Challenge: Download Cover Images Using wget

Goal:
- Scrape https://books.toscrape.com/
- Collect the first 10 books on the homepage
- Extract the title and image URL for each book
- Use the `wget` library to download and save images in a folder called 'images/'
- Use book titles (sanitized) as image filenames

Bonus:
- Add progress for each download
- Ensure folder is created if it doesn't exist
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import wget

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

def download_image(img_url, filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} - {e}")


def scrape_and_download_images():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    for book in books:
        title = book.h3.a['title']
        relative_img = book.find("img")["src"]
        img_url = urljoin(BASE_URL, relative_img)
        print(f"url - {img_url}")

        filename = sanitize_filename(title) + ".jpg"
        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"filepath - {filepath}")

        print(f"Downloading: {title}")
        # download_image(img_url, filepath)
        wget.download(img_url, filepath)
    print("All 10 books covers downloaded to images/")

if __name__ == "__main__":
    scrape_and_download_images()
```

---

### challenges/03_web_scraping/day_06.py

**File:** `day_06.py`

```python
"""
 Challenge: Quote of the Day Image Maker

Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in 'quotes/' directory using filenames like quote_1.png, quote_2.png, etc.


"""
import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"

def fetch_quotes():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    quote_data = []

    for q in quotes[:5]:
        text = q.find("span", class_="text").text.strip("“”")
        author = q.find("small", class_="author").text

        quote_data.append((text, author))

    return quote_data

def create_image(text, author, index):
    width, height = 800, 400
    backgroud_color = "#f8d77f"
    text_color = "#262626"

    image = Image.new("RGB", (width, height), backgroud_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()
    author_font = ImageFont.load_default()

    wrapped = textwrap.fill(text, width=60)
    author_text = f"- {author}"

    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)
    y_text += wrapped.count('\n') * 15 + 40
    draw.text((500, y_text), author_text, font=font, fill=text_color)

    # save image
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = os.path.join(OUTPUT_DIR, f"quote_{index+1}.png")
    image.save(filename)
    print(f"✅ saved: {filename}")


def main():
    quotes = fetch_quotes()
    for idx, (text, author) in enumerate(quotes):
        create_image(text, author, idx)

if __name__ == "__main__":
    main()
```

---

### challenges/03_web_scraping/day_07.py

**File:** `day_07.py`

```python
"""
 Challenge: Crypto Price Tracker with Graphs

Goal:
- Fetch live prices of the top 10 cryptocurrencies using CoinGecko's free public API
- Store prices in a CSV file with timestamp
- Generate a line graph for a selected coin over time (price vs. time)
- Repeatable — user can run this multiple times to log data over time

JSON handling, API usage, CSV storage, matplotlib graphing
"""
import os
import csv
from datetime import datetime
import requests
import matplotlib.pyplot as plt


API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

CSV_FILE = 'crypto_prices.csv'

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin['current_price']])
    print("✅ data saved to csv")


def plot_graph(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["coin"] == coin_id:
                times.append(row['timestamp'])
                prices.append(float(row['price']))

    if not times:
        print(f"No data found for {coin_id}")
        return
    
    plt.figure(figsize=(10,5))
    plt.plot(times, prices, marker='o')
    plt.tight_layout()
    plt.grid()
    plt.show()


def main():
    print("Fetching live crypto data....")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

    print("-" * 30)
    for coin in crypto_data:
        print(f"{coin['id']} - ${coin['current_price']}")
    print("-" * 30)

    choice = input("Enter the coinname to get graph: ").strip().lower()

    if choice:
        plot_graph(choice)


if __name__ == "__main__":
    main()
```

---

### challenges/03_web_scraping/day_08.py

**File:** `day_08.py`

```python
"""
depends on:
 - Day 7 of web scraping

Fetch crypto data every hour automatically

"""

import os
import csv
from datetime import datetime
import requests
import schedule
import time

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

CSV_FILE = 'crypto_prices.csv'

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin['current_price']])
    print("✅ data saved to csv")


def job():
    print("Fetching data hourly...")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

### challenges/03_web_scraping/day_09.py

**File:** `day_09.py`

```python
"""
 Challenge: Store & Search Crypto Prices in SQLite

Goal:
- Save hourly top 10 crypto prices into a local SQLite database
- Each record should include timestamp, coin ID, and price
- Allow the user to search for a coin by name and return the latest price

Teaches: SQLite handling in Python, data storage, search queries, API + DB integration
"""
import os
import csv
from datetime import datetime
import requests
import schedule
import time
import sqlite3

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

DB_NAME = 'crypto.db'

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TEXT,
                   coin TEXT,
                   price REAL
                   )
''')
    conn.commit()
    conn.close()

def save_to_database(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    for coin in data:
        cursor.execute('''
            INSERT INTO crypto_prices (timestamp, coin, price)
                       VALUES (?, ?, ?)
''', (timestamp, coin['id'], coin['current_price']))
        
    conn.commit()
    conn.close()
    print("Price saved to database")

def search_coin(coin_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT timestamp, price FROM crypto_prices
                   WHERE coin = ?
                   ORDER BY timestamp DESC
                   LIMIT 1
''', (coin_name, ))
    result = cursor.fetchone()
    conn.close()
    # print("RESULT RAW", result)
    if result:
        print(f"${result[1]} - {result[0]}")
    

def main():
    create_table()
    print("1. Fetch and store crypto data")
    print("2. Search latest price for a coin")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        data = fetch_crypto_data()
        save_to_database(data)
    elif choice == "2":
        coin_name = input("Enter coin name: ").strip().lower()
        search_coin(coin_name)
    else:
        print("Invalid option")


main()
```

---

### challenges/03_web_scraping/day_10.py

**File:** `day_10.py`

```python
import fitz

def read_pdf(file_path):
    doc = fitz.open(file_path)
    all_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        all_text += page.get_text()

    doc.close()
    return all_text

if __name__ == "__main__":
    file_path = "test.pdf"
    try:
        content =read_pdf(file_path)
        print("-" * 30)
        print(content)
        print("-" * 30)
    except Exception as e:
        print("Failed to read pdf, change that method")
```

---

### challenges/04_automation/day_01.py

**File:** `day_01.py`

```python
"""
 Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into subfolders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move

Teaches: File system operations, automation, file handling with `os` and `shutil`
"""
import os
import shutil

EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Images": [".png", ".jpeg", ".jpg"],
    "TextFiles": [".txt"]
}

def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return "Others"

def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        # write a check if file name is "day_01.py" then ignore this file

        if os.path.isfile(full_path):
            dest_folder = get_destination_folder(file)
            dest_path = os.path.join(folder_path, dest_folder)

            os.makedirs(dest_path, exist_ok=True)

            #move the file
            shutil.move(full_path, os.path.join(dest_path, file))
            print(f"Moved : {file} -> {dest_folder}/")


if __name__ == "__main__":
    folder = input("Enter the folder path or leave blank: ").strip()
    folder = folder or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid directory")
    else:
        sort_files(folder)
        print("✅ sorting completed")
```

---

### challenges/04_automation/day_02.py

**File:** `day_02.py`

```python
"""
Challenge: Batch Rename Files in a Folder

Goal:
- Scan all files in a selected folder
- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...
- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")
- Preview before renaming
- Optional: allow undo (save original names in a file)

Teaches: File iteration, string formatting, renaming, user input
"""
import os

def batch_rename(folder, base_name, extension):
    files = [f for f in os.listdir(folder) if f.lower().endswith(extension.lower())]
    files.sort() # this will not do much

    if not files:
        print("NO files found in dir")
        return
    
    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        print(f"{file} => {new_name}")
    confirm = input("Press (y) to confirm or (n) to reject").strip().lower()

    if confirm != 'y':
        print("Cancel")
        return
    
    for i, file in enumerate(files, start=1):
        src = os.path.join(folder, file)
        new_name = f"{base_name}_{i}{extension}"
        dest = os.path.join(folder, new_name)
        os.rename(src, dest)
    print(f"Renamed {len(files)} files successfully")

if __name__ == "__main__":
    folder = input("Enter folder path or learn blank for current folder: ").strip() or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid folder")
    else:
        base_name = input("Enter base name for files: ").strip()
        extension = input("Enter extension name for files: ").strip()

        batch_rename(folder, base_name, extension)

```

---

### challenges/04_automation/day_03.py

**File:** `day_03.py`

```python
"""
 Challenge: Auto File Organizer with Watchdog

Goal:
- Monitor a folder (e.g., Downloads/Desktop)
- When a new file is added:
    - Move PDFs to /PDFs
    - Move Images to /Images
    - Move ZIP files to /Archives
    - Everything else goes to /Others

Teaches: Folder monitoring, real-time automation, event-driven design
Tools: watchdog, shutil, os
"""

import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/Downloads")

FILE_DESTS = {
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images',
}


class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        filepath = event.src_path
        ext = os.path.splitext(filepath)[1].lower()

        dest_folder = FILE_DESTS.get(ext, 'Others')
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)
        os.makedirs(full_dest, exist_ok=True)
        move_to = os.path.join(full_dest, os.path.basename(filepath))
        try:
            shutil.move(filepath, move_to)
            # print message
        except:
            print("Failed to move")
    
if __name__ == "__main__":
    print(f"Watching folder: {WATCH_FOLDER}")
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

---

### challenges/04_automation/day_04.py

**File:** `day_04.py`

```python
"""
 Challenge: Real-Time System Resource Monitor

Goal:
- Monitor your system's CPU, RAM, and Disk usage
- Print updates every few seconds
- Warn user if CPU or RAM usage exceeds 80%
- Runs in terminal as a live dashboard

Teaches: psutil, formatting, real-time monitoring, conditional logic
Tools: psutil, time
"""
import psutil
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_stats():
    print("🔥" * 30)
    print("⭐️ System Resource Monitor ⭐️")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print(f"CPU USAGE: {cpu}")
    print(f"RAM USAGE: {ram.percent}% ( {round(ram.used / 1e9, 2)} GB used of {round(ram.total / 1e9, 2)} GB)")
    print(f"DISK USAGE: {disk.percent}% ( {round(disk.used / 1e9, 2)} GB used of {round(disk.total / 1e9, 2)} GB)")
    print("🔥" * 30)

if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            show_stats()
            time.sleep(3)
    except KeyboardInterrupt:
        print("Monitoring Stopped.....")
```

---

### challenges/05_data_science/day_02.py

**File:** `day_02.py`

```python
import numpy as np
import pandas as pd

np.random.seed(42)

years = np.random.uniform(0.5, 10, 100).round(2)

salaries = (30000 + years * 6000 + np.random.normal(0, 4000, size=100) ).round(2)

df = pd.DataFrame({
    "YearsExperience": years,
    "Salary": salaries
})
df.to_csv("experience_salary.csv", index=False)
print("Data saved in file ✅")
```

---

### challenges/05_data_science/day_03.py

**File:** `day_03.py`

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# load data set
data = pd.read_csv("experience_salary.csv")

X = data[["YearsExperience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(X, y)

data["PredictedSalary"] = model.predict(X)

print("Model Coefficient (slope)", round(float(model.coef_[0]), 2))
print("Model INtercept (base salary)", round(float(model.intercept_), 2))

plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, data["PredictedSalary"], color="red", label="Regression line")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

### challenges/05_data_science/day_04.py

**File:** `day_04.py`

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

data = pd.read_csv("experience_salary.csv")

X = data[["YearsExperience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(X, y)

st.title("Salary Predictor based on experience")
st.write("Enter your years of experience to predict your salary:")

years_input = st.number_input("Years of experience", min_value=0.0, max_value=50.0, step=0.1)

if years_input:
    print(years_input)

    predicted_salary = model.predict([[years_input]])[0]
    st.success(f"Estimated Salary: {predicted_salary}")

st.subheader("Regression Line")

fig, ax = plt.subplots()
ax.scatter(X, y, color="blue", label="Actual Data")
ax.plot(X, model.predict(X), color="red", label="Regression line")
ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.legend()

st.pyplot(fig)
```

---

### challenges/05_data_science/day_05.py

**File:** `day_05.py`

```python
import pandas as pd
import numpy as np
import random

toxic_comments = [
    "You're so dumb", "This is trash", "Worst video ever", "Stop making content", "You sound horrible",
    "Clickbait title", "Can't believe people like this", "Waste of time", "Cringe content", "You're such a loser"
]

supportive_comments = [
    "This helped me a lot!", "You're amazing!", "Best tutorial I've seen", "Thanks for the content!",
    "Keep up the great work", "So clear and helpful", "Awesome explanation", "I learned a lot!", "Much appreciated!", "Legend!"
]

data = []

for i in range(50):
    data.append({"comment": random.choice(toxic_comments), "label": "toxic"})
    data.append({"comment": random.choice(supportive_comments), "label": "support"})

df = pd.DataFrame(data)
df.to_csv("youtube_comments.csv", index=False)
print("✅ Data saved successfully")
```

---

### challenges/05_data_science/day_06.py

**File:** `day_06.py`

```python
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


df = pd.read_csv("youtube_comments.csv")

X_train, X_test, y_train, y_test = train_test_split(df['comment'], df['label'], test_size=0.2, random_state=42)

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print(f"Model tained. Accuracy: {round(acc * 100, 2)}%")
```

---

### challenges/05_data_science/day_07.py

**File:** `day_07.py`

```python
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import streamlit as st

@st.cache_resource
def load_model():
    df = pd.read_csv("youtube_comments.csv")
    model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
    ])
    model.fit(df['comment'], df['label'])
    return model

model = load_model()

st.title("Youtube comment classifier")
st.write("Classify your comment as Toxic or supportive")
user_input = st.text_area("Enter a youtube comment")

if user_input:
    prediction = model.predict([user_input])[0]
    if prediction == "toxic":
        st.error("This comment is likely **Toxic**")
    else:
        st.success("This comment is **Supportive**")


```

---

### challenges/05_data_science/day_08.py

**File:** `day_08.py`

```python
import pandas as pd

data = [
    {
        "title": "The Silent Forest",
        "author": "Jane Hill",
        "genre": "Mystery",
        "description": "A detective uncovers secrets hidden deep in the woods while chasing a serial killer."
    },
    {
        "title": "Spacebound",
        "author": "Rico Vega",
        "genre": "Science Fiction",
        "description": "An astronaut embarks on a mission to Mars but discovers an ancient alien presence."
    },
    {
        "title": "Love in Paris",
        "author": "Emily Rose",
        "genre": "Romance",
        "description": "A love story between a local baker and a traveler unfolds in the heart of Paris."
    },
    {
        "title": "Quantum Heist",
        "author": "Leo Hunt",
        "genre": "Thriller",
        "description": "A group of hackers plans a digital heist targeting the world's most secure quantum server."
    },
    {
        "title": "Mystic Academy",
        "author": "Lara Moon",
        "genre": "Fantasy",
        "description": "A young girl discovers she has magical powers and is taken to an academy for gifted spellcasters."
    },
    {
        "title": "The Digital Mind",
        "author": "Alan Neural",
        "genre": "Science Fiction",
        "description": "An AI begins to question its creators and the meaning of consciousness."
    },
    {
        "title": "Fog Over London",
        "author": "Claire Black",
        "genre": "Mystery",
        "description": "Set in Victorian London, a private investigator unravels political conspiracies amid murders."
    },
    {
        "title": "Beneath the Waves",
        "author": "Diana Coast",
        "genre": "Adventure",
        "description": "An underwater archaeologist discovers an ancient city lost in the ocean."
    },
    {
        "title": "Heart Strings",
        "author": "Ella Harmony",
        "genre": "Romance",
        "description": "Two musicians from rival bands fall in love during a national tour."
    },
    {
        "title": "Dark Code",
        "author": "Nick Cipher",
        "genre": "Thriller",
        "description": "A cybersecurity expert is drawn into a global web of espionage and hidden messages."
    }
]

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print("✅ Book dataset created")
```

---

### challenges/05_data_science/day_09.py

**File:** `day_09.py`

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("books.csv")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title'])


def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[['title', 'author']].iloc[book_indices]
```

---

### challenges/05_data_science/day_10.py

**File:** `day_10.py`

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

df = pd.read_csv("books.csv")
df['title'] = df['title'].str.strip()
df['description'] = df['description'].fillna("")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()


def get_recommendations(title, df,  cosine_sim, indices):
    title = title.strip().lower()

    if title not in indices.index:
        return f"{title} not found in dataset"
    
    idx = indices.loc[title]
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]


    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[['title', 'author']].iloc[book_indices]


st.title("Book Recommendation Engine")
st.write("Enter a book title and get similar recommendation")

select_book = st.text_input("Book: Title")

if select_book:
    results = get_recommendations(select_book, df, cosine_sim, indices)

    if isinstance(results, pd.DataFrame):
        st.table(results)
    else:
        st.warning(results)
```

---

### challenges/06_url_shortner/app.py

**File:** `app.py`

```python
from flask import Flask, request, redirect, render_template
import random
import string

from models import (
    init_db, 
    insert_url, 
    get_url, 
    get_all_urls, 
    increment_visit_count, 
    delete_url_by_code
    )

app = Flask(__name__)

init_db()

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        orginal_url = request.form['url']
        short_code = generate_short_code()
        insert_url(orginal_url, short_code)
        return redirect("/")
    all_urls = get_all_urls()
    return render_template('index.html', all_urls=all_urls)

@app.route("/about")
def about():
    return 'this is an amazing course on python - Udemy'

@app.route('/<short_code>')
def redirect_url(short_code):
    url_data = get_url(short_code)
    if url_data:
        increment_visit_count(short_code)
        return redirect(url_data[1])
    return render_template('404.html'), 404

@app.route('/delete/<short_code>', methods=['POST'])
def delete_url(short_code):
    delete_url_by_code(short_code)
    return redirect("/")


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8000
        )
```

---

### challenges/06_url_shortner/models.py

**File:** `models.py`

```python
import sqlite3


DB_NAME = 'database.db'


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     original_url TEXT NOT NULL,
                     short_code TEXT UNIQUE NOT NULL,
                     visit_count INTEGER DEFAULT 0
                     )
        ''')

def insert_url(original_url, short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            INSERT INTO urls (original_url, short_code)
                     VALUES (?, ?)
        ''', (original_url, short_code))

def get_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,))
        return cur.fetchone()
    
def increment_visit_count(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            UPDATE urls
            SET visit_count = visit_count + 1
            WHERE short_code = ?         
        ''', (short_code,))

def get_all_urls():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('SELECT original_url, short_code, visit_count FROM urls ORDER by id DESC')
        return cur.fetchall()
    
def delete_url_by_code(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE from urls WHERE short_code = ?', (short_code,))
```

---
