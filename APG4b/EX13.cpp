#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    int ap = 0;
    rep(i, N) {
        cin >> A.at(i);
        ap += A.at(i);
    }
    ap /= N;
    rep(i, N){
        cout << abs(ap - A.at(i)) << endl;
    }
}
