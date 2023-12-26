numbers = input()
a, b, c, d = int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])
operants = ['+', '-']
for operant1 in operants:
    for operant2 in operants:
        for operant3 in operants:
            if eval(str(a) + operant1 + str(b) + operant2 + str(c) + operant3 + str(d)) == 7:
                print(str(a) + operant1 + str(b) + operant2 + str(c) + operant3 + str(d) + '=7')
                exit()