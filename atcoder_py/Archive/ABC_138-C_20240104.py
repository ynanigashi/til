num_of_materials = int(input())
materials = list(map(int, input().split()))
materials.sort()
for i in range(num_of_materials-1):
    materials[i+1] = (materials[i] + materials[i+1])/2
print(materials[-1])