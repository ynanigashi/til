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
    set<int> d;
    rep(i, n) {
        int j;
        cin >> j;
        d.insert(j);
    }
    cout << d.size() <<endl;
    return 0;
}