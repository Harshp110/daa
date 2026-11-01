n = int(input("Enter number of items: "))

weight = []
profit = []

for i in range(n):
    w, p = map(int, input("Enter weight and profit: ").split())
    weight.append(w)
    profit.append(p)

capacity = int(input("Enter knapsack capacity: "))

dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weight[i - 1] <= w:
            include = profit[i - 1] + dp[i - 1][w - weight[i - 1]]
            exclude = dp[i - 1][w]
            dp[i][w] = max(include, exclude)
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Profit:", dp[n][capacity])
