#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
// 最大値：86を入力すると帰ってこない。。。
ll recursion(int N) {
    if(N==0) return 2;
    if(N==1) return 1;
    return recursion(N-1) + recursion(N-2);
}

int main() {
    int N;
    cin >> N;
    cout << recursion(N) << endl;
}
