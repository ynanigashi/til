#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    int n, k;
    cin >> n >> k;
    vi a(n);
    rep(i, n) cin >> a.at(i);
    rep(i, 1<<n) {
        int count = 0;
        rep(j, n) {
            if(i & (1<<j)) {
                count += a.at(j);
            }
        }
        if(count == k) {
            cout << "Yes" << endl;
            return 0;
        }
    } 
    cout << "No" << endl;
}
