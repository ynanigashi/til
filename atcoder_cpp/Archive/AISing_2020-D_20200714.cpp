#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vivi = vector<vi>;

int pcnt(int x){
    return __builtin_popcount(x);
}

int f(int x) {
    if(x == 0) return 0;
    return f(x%pcnt(x))+1;
}

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vi x(n);
    rep(i, n) x.at(i) = s.at(i)-'0';
    int popcnt = 0;
    //最初に入力された二進数Xのpopcountを求める
    rep(i, n) popcnt += x.at(i);
    vi ans(n);
    //Oと1で処理
    rep(b,2){
        int npopcnt = popcnt;
        if(b == 0) npopcnt++; else npopcnt--;
        //npopcntが０以下の場合の例外処理
        if(npopcnt <= 0) continue;
        //元の割った余り？
        int r0 = 0;
        rep(i, n){
            r0 = (r0*2)%npopcnt;
            r0 += x.at(i); 
        }
        int k = 1;
        for(int i = n-1; i >= 0; i--) {
            if(x.at(i) == b) {
                int r = r0;
                if(b == 0) r = (r+k)%npopcnt;
                //r-kはマイナスになる可能性があるのでnpopcntを足す
                else r =(r-k+npopcnt)%npopcnt;
                ans.at(i) = f(r) + 1;
            }
            k = (k*2)%npopcnt;
        }
    }
    rep(i,n) cout << ans.at(i) << endl;
}
