#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int N;
    cin >> N;
    vector<int> div_list(N+1);
    for (int i = 1; i <= N; i++) {
        for(int j = i; j <= N; j += i) div_list.at(j) += 1;
    }
    ll ans = 0;
    for (int i = 1; i <= N; i++) ans += ll(i)*div_list.at(i);
    cout << ans << endl;
}
