#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

int main() {
    string s, t;
    cin >> s >> t;
    int ans = t.size();
    rep(i, s.size()) {
        if(i + t.size() > s.size()) break;
        int cnt = 0;
        rep(j, t.size()) if(s[i + j] != t[j]) cnt++;
        ans = min(ans, cnt);
    }
    cout << ans << endl;
    return 0;
}
