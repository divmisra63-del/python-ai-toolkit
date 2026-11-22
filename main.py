prices = [25, 40, 15, 60, 10]

total_products = 0
total_cost = 0
highest_price = prices[0]
lowest_price = prices[0]
final_price = 0

for products in prices:
    total_products = total_products +1
    total_cost = total_cost + products
    if highest_price <= products:
        highest_price = products
    if lowest_price >= products:
            lowest_price = products
    if total_cost > 100:
         final_price = total_cost - (total_cost*0.1)
         
         

print(f"total products:{total_products}")
print(f"total cost:{total_cost}")
print(f"most expensive:{highest_price}")
print(f"cheapest:{lowest_price}")
print(f"discount:{total_cost*0.1}")
print(f"Final amount:{final_price}")
