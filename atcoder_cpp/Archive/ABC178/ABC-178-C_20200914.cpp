#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll mod=1000000007;

ll modpow(ll a, ll n) {
    ll res = 1;
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
    ll ans = modpow(10, n) - (modpow(9, n)*2 - modpow(8, n));
    ans %= mod;
    if(ans < 0) ans += mod;
    cout << ans << endl;
    return 0;
}
