#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

int main() {
    int n;
    ll d;
    cin >> n >> d;
    int answer = 0;
    rep(i, n) {
        ll x, y;
        cin >> x >> y;
        if(x*x + y*y <= d * d) answer++;
    }
    cout << answer << endl;
}
