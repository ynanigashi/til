#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

const ll INF = 1e18;

vector<ll> calc(vector<P> a) {
    int n = a.size();
    vector<ll> res(n+1, INF);
    rep(s, 1<<n) {
        vector<int> p(1,0);
        rep(i, n) if(s>>i&1) p.push_back(a.at(i).first);
        ll now = 0;
        rep(i, n) {
            int m = 1e9;
            rep(j, p.size()) m = min(m, abs(p.at(j)-a.at(i).first));
             now += ll(m)*a.at(i).second;
        }
        int b = p.size()-1;
        res.at(b) = min(res.at(b), now);
    }
    return res;
}

int main() {
    int n;
    vi x(n), y(n), p(n);
    rep(i, n) cin >> x.at(i) >> y.at(i) >> p.at(i);
    vector<ll> ans(n+1, INF);
    rep(s, 1<<n) {
        vector<P> ax, ay;
        rep(j, n) {
            if(s>>i&1) ax.emplace_back(x.at(i), p.at(i));
            else ay.emplace_back(y.at(i), p.at(i));
        }
        vector<ll> dx = calc(ax);
        vector<ll> dy = calc(ay);
        rep(i, dx.size()) rep(j,dy.size()) {
            ans.at(i+j) = min(ans.at(i+j), dx.at(i)+dy.at(j));
        }
    }
    rep(i, n+1) {
        cout << ans.at(i) << endl;
    }
    return 0;
}