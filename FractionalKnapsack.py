n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight, profit = map(float, input("Enter weight and profit: ").split())
    ratio = profit / weight
    items.append((weight, profit, ratio))

capacity = float(input("Enter knapsack capacity: "))

items.sort(key=lambda x: x[2], reverse=True)

total_profit = 0

for weight, profit, ratio in items:
    if capacity <= 0:
        break

    if weight <= capacity:
        capacity -= weight
        total_profit += profit
    else:
        total_profit += ratio * capacity
        capacity = 0

print("Maximum Profit:", round(total_profit, 2))
