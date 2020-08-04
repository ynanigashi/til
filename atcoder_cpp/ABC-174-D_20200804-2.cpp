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
    int red = 0, white = 0;
    vi count(n);
    rep (i, n) {
        if (s.at(i) == 'R') red++;
        else white++;
        count.at(i) = white;
    }
    if (red == 0) cout << 0 << endl;
    else cout << count.at(red - 1) << endl;
    return 0;
}
