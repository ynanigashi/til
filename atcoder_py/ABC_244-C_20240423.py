n = int(input())
n2p1 = [i for i in range(1, 2 * n + 2)]
while True:
    output = n2p1[0]
    n2p1.remove(output)
    print(output)
    input_ = int(input())
    if input_ == 0:
        break
    n2p1.remove(input_)
