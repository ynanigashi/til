def f(N):
    if N == 0: return ""
    N -= 1
    return f(N//26) + chr(97 + N%26)

N = int(input())
print(f(N))