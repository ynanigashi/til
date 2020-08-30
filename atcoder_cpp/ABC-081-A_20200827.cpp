#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

int main() {
    string s;
    cin >> s;
    int ans = 0;
    for (auto c : s){
        if (c == '1') ans++;
    }
    cout << ans << endl;
    return 0;
}
