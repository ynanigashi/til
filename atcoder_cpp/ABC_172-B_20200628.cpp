#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    string S, T;
    cin >> S >> T;
    int ans = 0;
    rep(i, S.size()){
        if(S.at(i) != T.at(i)) ans++;
    }
    cout << ans << endl;
}
