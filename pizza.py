# Your code below:

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

# How many pizzas cost $2/slice?
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# How long is the menu list of pizzas?
num_pizzas = len(toppings)

# Make a tagline
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Convert the pizzas and prices to a 2-D list.

pizza_and_prices = [[2.00, "pepperoni"], [6.00, "pineapple"], [1.00, "cheese"], [3.00, "sausage"], [2.00, "olives"], [7.00, "anchovies"], [2.00, "mushrooms"]]

print(pizza_and_prices)

# Sort pizza_and_prices so that the pizzas are in order of increasing price.

pizza_and_prices.sort()
print(pizza_and_prices)

# Save the cheapest pizza on the menu to a variable.

cheapest_pizza = pizza_and_prices[0]

# Get the last item of the list (most expensive) and store it in a variable.

priciest_pizza = pizza_and_prices[-1]

# Remove the most expensive item from the menu because someone bought it.

pizza_and_prices.pop()

print(pizza_and_prices)

# Add "peppers" to the menu with the price of $2.50 a slice.  Make sure it's positioned correctly as the list originally sorted.

pizza_and_prices.append([2.5, "peppers"])

print(pizza_and_prices)

# Pick the three cheapest pizzas knowing that the pizza_and_prices list are already sorted by price.

three_cheapest = pizza_and_prices[:3]

print(three_cheapest)

