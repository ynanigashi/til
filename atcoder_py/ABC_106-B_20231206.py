def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def is_diversors_8_odd(n):
    return count_divisors(n) == 8 and n % 2 == 1

# diversors_8_odd = [i for i in range(1, 201) if is_diversors_8_odd(i)]
# print(diversors_8_odd)

diversors_8_odd = [105, 135, 165, 189, 195]
results = [i in diversors_8_odd for i in range(201)]
n = int(input())
print(sum(results[:n+1]))