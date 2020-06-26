#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, S;
    cin >> N >> S;
    vector<int> A(N);
    rep(i, N) cin >> A.at(i);
    vector<int> P(N);
    rep(i, N) cin >> P.at(i);
    int ans = 0;
    rep(i, N){
        rep(j, N){
            if(A.at(i) + P.at(j) == S){
                ans += 1;
            }
        }
    }
    cout << ans << endl;

}
