#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    vector<int> H(3);
    rep(i, 3) cin >> H.at(i);
    sort(H.begin(), H.end());
    cout << H.end() - H.begin() << endl;
}
