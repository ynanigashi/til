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
    int ans = 0;
    rep(i, 3) if (s[i] == 'R') ans++;
    if(ans == 2 && s[1] == 'S') cout << 1 << endl;
    else cout << ans << endl;
}
