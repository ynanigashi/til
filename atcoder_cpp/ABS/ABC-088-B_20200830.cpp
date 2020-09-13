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
    vi a(n);
    rep(i, n) cin >> a.at(i);
    sort(a.begin(), a.end());
    reverse(a.begin(), a.end());
    int alice = 0, bob = 0;
    rep(i, n){
        if(i%2 == 0) alice += a.at(i);
        else bob += a.at(i);
    }
    cout << alice - bob << endl; 
    return 0;
}