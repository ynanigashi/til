#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int N;
    cin >> N;
    map<string, int> ans;
    rep(i, N) {
        string s;
        cin >> s;
        ans[s]++;
    }
    for (string s: {"AC", "WA", "TLE", "RE"}) {
        cout << s << " x " << ans[s] << endl;
    }
}
