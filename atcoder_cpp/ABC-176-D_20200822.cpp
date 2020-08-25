#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    int h, w, m;
    cin >> h >> w >> m;
    vi sum_h(h), sum_w(w);
    vvi hw(h, vi(w));
    rep(i, m){
        int j, k;
        cin >> j >> k;
        j--;
        k--;
        hw[j][k] = 1;
        sum_h[j]++;
        sum_w[k]++;
    }
    int ans = 0;
    rep(i, h)rep(j, w){
        int dest;
        dest = sum_h[i] + sum_w[j];
        if(hw[i][j] == 1) dest--;
        ans = max(ans, dest);
    }
    cout << ans << endl;
}
