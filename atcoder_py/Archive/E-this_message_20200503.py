import itertools
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    h_list = list(map(int, input().split()))
    c_list = list(itertools.combinations(range(N),2))
    ans = 0

    for c in c_list:
            if abs(c[0] - c[1]) == h_list[c[0]] + h_list[c[1]]:
                ans += 1

    print(ans)