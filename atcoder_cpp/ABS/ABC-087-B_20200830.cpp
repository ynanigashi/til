#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

int main() {
    int a, b, c, x;
    cin >> a >> b >> c >> x;
    a = min(a, x/500);
    b = min(b, x/100);
    c = min(c, x/50);
    int ans = 0;
    for(int i = 0; i <= a; i++){
        for(int j = 0; j <= b; j++){
            for(int k = 0; k <= c; k++){
                if(i*500 + j*100 + k*50 == x) ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}