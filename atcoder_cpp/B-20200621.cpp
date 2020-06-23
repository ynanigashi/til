#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
 
int main() {
    int N, K;
    cin >> N >> K;
    vector<int> P(N);
    rep(i, N){
        cin >> P.at(i);
    }
    sort(P.begin(), P.end());
    int ans = 0;
    rep(i, K){
        ans += P.at(i);
    }
    cout << ans << endl;
 
}