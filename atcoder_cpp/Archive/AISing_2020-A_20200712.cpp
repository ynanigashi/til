#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int L, R, d;
    cin >> L >> R >> d;
    cout << R/d - (L-1)/d << endl;
}
