group_a = [1, 3, 5, 7, 8, 10, 12]
group_b = [4, 6, 9, 11]
group_c = [2]
groups = {'a':group_a, 'b':group_b, 'c':group_c}

def get_group(n: str):
    n = int(n)
    for group_name, group_numbers in groups.items():
        if n in group_numbers: return group_name

    return -1

x, y = map(get_group, input().split()) 
print('Yes' if x == y else 'No')