#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    int n;
    string s;
    cin >> n >> s;
    int a = 0, b = 0;
    rep(i, n) if (s[i] == 'R') a++;
    int ans = max(a,b);
    rep (i, n) {
        if (s[i] == 'R') a--;
        else b++;
        int now = max(a, b);
        ans = min(ans, now);
    }
    cout << ans << endl;
    return 0;
}
