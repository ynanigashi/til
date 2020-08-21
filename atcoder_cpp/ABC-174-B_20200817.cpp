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
    vi l(n);
    rep(i, n) cin >> l.at(i);
    int ans = 0;
    rep(i, n)rep(j, n)rep(k, n) {
        if(i < j && j < k) {
            if(l.at(i) == l.at(j)) continue;
            if(l.at(j) == l.at(k)) continue;
            if(l.at(k) == l.at(i)) continue;
            if((ll)l.at(i) + l.at(j) + l.at(k) <= max({l.at(i), l.at(j), l.at(k)}) * 2) continue;
            ans++;
        }

    }
    cout << ans << endl;
}
