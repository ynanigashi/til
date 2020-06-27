#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<char>> res(N, vector<char>(N, '-'));
    for (int i = 0; i < M; i++) {
        int A, B;
        cin >> A >> B;
        res.at(A-1).at(B-1) = 'o';
        res.at(B-1).at(A-1) = 'x';
  }
  rep (i, N){
        rep(j, N){
            cout << res.at(i).at(j);
            if(j == N-1) {
                cout << endl;
            } else {
                cout << ' ';
            }
      }
  }
}
