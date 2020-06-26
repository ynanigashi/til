#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    vector<int> A(5);
    rep(i, 5) cin >> A.at(i);
    string ans;
    ans = "NO";
    rep(i,4){
        if(A.at(i) == A.at(i+1)) {
            ans = "YES";
            break;
        }
    }
    cout << ans << endl;
}
