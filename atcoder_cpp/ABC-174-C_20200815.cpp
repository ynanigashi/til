#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    ll x, k, d;
    cin >> x >> k >> d;
    x = abs(x);
    if( x >= k*d ) {
        cout << x - k*d << endl;
        return 0;
    }
    if((k - (x/d))%2 == 0) cout << x%d << endl;
    else cout << abs(x%d - d) << endl;
}
