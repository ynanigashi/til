#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

int sum_of_digits(int i){
    if(i < 10) return i;
    return sum_of_digits(i/10) + i%10;
}

int main() {
    int n, a, b;
    cin >> n >> a >> b;
    int ans = 0;
    rep(i, n+1){
        int sum = sum_of_digits(i);
        if( a <= sum && sum <= b) ans += i;
    }
    cout <<  ans << endl;
    return 0;
}