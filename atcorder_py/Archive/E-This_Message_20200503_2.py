input()
A = [int(h) for h in input().split()]
iph_dic = {}
pair_of_spies = 0

for i, h in enumerate(A):
    if i - h in iph_dic:
        pair_of_spies += iph_dic[i - h]
    if i + h in iph_dic:
        iph_dic[i + h] += 1
    else:
        iph_dic[i + h] = 1

print(pair_of_spies)