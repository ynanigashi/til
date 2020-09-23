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
    int r = sqrt(n);
    int cnt = 0;
    for(int i = 1; i <= r; i++){
        for(int j = i; j < n; j++){
            if(i * j < n) cnt++;
            else break;
            if( i != j) cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}
