#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int N;
    cin >> N;
    int ans = 0;
    for(int i = 1; i < N+1;i++ ){
        int a;
        cin >> a;
        if(i%2 == 1){
            if(a%2 == 1) ans++;
        }
    }
    cout << ans << endl;
}
