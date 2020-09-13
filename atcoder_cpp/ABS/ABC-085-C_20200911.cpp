#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

int main() {
    int n, y;
    cin >> n >> y;
    bool break_flg = false;
    for(int i = 0; i <= n; i++){
        for(int j = 0; j <= n - i; j++){
                int k = n -(i + j);
                if(i*10000 + j*5000 + k*1000 == y){
                    cout << i << " " << j << " " << k << endl;
                    break_flg = true;
                    break;
                }
        }
        if(break_flg) break;
    }
    if(!break_flg)cout << -1 << " " << -1 << " " << -1 << endl;
    return 0;
}