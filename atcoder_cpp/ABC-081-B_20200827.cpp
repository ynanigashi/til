#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

int main() {
    int n;
    cin >> n;
    vi a(n);
    rep(i, n) cin >> a.at(i);
    int ans = 0;
    while (1){
        bool break_flg = false;
        rep(i, n) if(a.at(i)%2 == 1) break_flg = true;
        if(break_flg) break;
        ans++;
        rep(i, n) a.at(i) /= 2;
    }
    cout << ans << endl;
    return 0;
}
