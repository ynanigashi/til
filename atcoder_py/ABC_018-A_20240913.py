a = int(input())
b = int(input())
c = int(input())
list = [a, b, c]
sorted_list = sorted(list, reverse=True)
print(sorted_list.index(a) + 1)
print(sorted_list.index(b) + 1)
print(sorted_list.index(c) + 1)