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
    int cnt = 0;
    string ans = "No";
    rep(i, n){
        int a, b;
        cin >> a >> b;
        if(a == b) cnt++;
        else cnt = 0;
        if(cnt == 3){
            ans = "Yes";
            break;
        }
    }
    cout << ans << endl;
    return 0;
}
