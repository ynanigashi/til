N = int(input())
def kaijo1(i, ans):
    if i == 1:
        print(ans)
    else:
        ans *= i
        kaijo1(i-1, ans)

def kaijo2(i):
    if i == 1:
        return 1
    return i * kaijo2(i - 1)

kaijo1(N,1)
print(kaijo2(N))