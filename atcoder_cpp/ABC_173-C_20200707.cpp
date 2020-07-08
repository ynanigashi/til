#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int H, W, K;
    cin >> H >> W >> K;
    vector<string> C(H);
    rep(i, H) cin >> C.at(i);
    int ans = 0;
    rep(i, 1<<H) rep(j, 1<<W) {
        int cnt = 0;
        rep(m, H) rep(n, W){
            if(i>>m&1) continue;
            if(j>>n&1) continue;
            if(C[m][n] == '#') cnt++;
        }
        if (cnt == K) ans++;
    }
    cout << ans << endl;
}