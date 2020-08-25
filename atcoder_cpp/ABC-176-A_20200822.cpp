#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    int n, x, t;
    cin >> n >> x >> t;
    if (n%x == 0) cout << n/x*t << endl;
    else cout << (n/x+1)*t << endl;
}
