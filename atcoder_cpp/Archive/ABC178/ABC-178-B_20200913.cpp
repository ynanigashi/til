#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

int main() {
    ll a, b, c, d;
    cin >> a >> b >> c >> d;
    ll ans = LLONG_MIN;
    ll ac = a * c;
    ans = max(ans, ac);
    ll ad = a * d;
    ans = max(ans, ad);
    ll bc = b * c;
    ans = max(ans, bc);
    ll bd = b * d;
    ans = max(ans, bd);
    if(a <= 0 and b >= 0) ans = max(ans, (ll)0);
    if(c <= 0 and d >= 0) ans = max(ans, (ll)0);
    cout << ans << endl;
    return 0;
}
