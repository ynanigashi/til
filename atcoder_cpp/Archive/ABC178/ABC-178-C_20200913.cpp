#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

long long modpow(long long a, long long n, long long mod) {
    long long res = 1;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}

int main() {
    int n;
    cin >> n;
    if (n <= 1) {
        cout << 0 << endl;
        return 0;
    }
    if (n == 2) {
        cout << 2 << endl;
        return 0;
    }

    if(n == 3) {
        cout << 54 << endl;
    }
    ll ans = 48;
    rep(i, n - 3){
        ans = (ans * 10) % 1000000007;
    }
    ans += modpow(2, n, 1000000007);
    ans %= 1000000007;
    cout << ans-2 << endl;
    return 0;
}
