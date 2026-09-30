python
# Simple Bill Calculator

price = float(input("50: "))
quantity = int(input("3: "))

total = price * quantity

print(f"{quantity} items at {price:50} each = {total:.150}")
