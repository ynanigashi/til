num_of_vertices = int(input())
relations = [set() for _ in range(num_of_vertices)]
for _ in range(num_of_vertices - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    relations[a].add(b)
    relations[b].add(a)
num_of_relations = [len(relation) for relation in relations]
max_num_of_relations = max(num_of_relations)
print('Yes' if max_num_of_relations == num_of_vertices - 1 else 'No')