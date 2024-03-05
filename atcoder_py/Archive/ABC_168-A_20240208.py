hon = [2,4,5,7,9]
pon = [0,1,6,8]
# bon = [3]
n = int(input()[-1])
print('hon' if n in hon else 'pon' if n in pon else 'bon')