# shipping.py
# Created by: rgpascual
# Input weight of the package to send

weight = 41.5
cost = 0.0
drone_cost = 0.0

# Ground Shipping Prices

if weight < 2.0:
  cost = 1.50
elif weight > 2.0 and weight <= 6.0:
  cost = 3.00
elif weight > 6.0 and weight <= 10.0:
  cost = 4.00
else :
  cost = 4.75 

# Premium Shipping

premium_cost = 125.00

# Drone Shipping

if weight < 2.0:
  drone_cost = 4.50
elif weight > 2.0 and weight <= 6.0:
  drone_cost = 9.00
elif weight > 6.0 and weight <= 10.0:
  drone_cost = 12.00
else :
  drone_cost = 14.25 

# Calculate Costs

cost *= weight
drone_cost *= weight
cost += 20.00

# Output of results

print(cost)
print(premium_cost)
print(drone_cost)

