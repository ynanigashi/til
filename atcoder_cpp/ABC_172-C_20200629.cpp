#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int N, M, K;
    cin >> N >> M >> K;
    vector<int> A(N);
    vector<int> B(M);
    rep(i, N) cin >> A[i];
    rep(i, M) cin >> B[i];

    ll tot = 0;
    rep(i, M) tot += B[i];

    int j = M;
    int ans = 0;
    rep(i, N+1) {
        while (j > 0 && tot > K) {
            j -= 1;
            tot -= B[j];
        }
        if (tot > K) break;
        ans = max(ans, i+j);
        if (i == N) break;
        tot += A[i];
    }
    cout << ans << endl;

}
