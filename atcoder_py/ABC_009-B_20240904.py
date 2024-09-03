num_of_inputs = int(input())
prices = [int(input()) for _ in range(num_of_inputs)]
prices = list(set(prices))
prices.sort(reverse=True)
print(prices[1])