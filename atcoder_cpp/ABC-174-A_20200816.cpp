#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    string s;
    cin >> s;
    int count = 0, ans = 0;
    rep(i, s.length()) {
        if(s[i] == 'R') count++;
        else count = 0;
        ans = max(ans, count);
    }
    cout << ans << endl;
}
