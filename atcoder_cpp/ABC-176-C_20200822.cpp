#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    int n;
    cin >> n;
    vi a(n);
    rep(i, n) cin >> a.at(i);
    int previous = a.at(0);
    ll ans = 0;
    for (int i = 1; i < n; i++){
        if (previous > a.at(i)) {
            ans += previous - a.at(i);
        }
        else previous = a.at(i);
    }
    cout << ans << endl;
}
