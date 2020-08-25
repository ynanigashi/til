#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    string n;
    cin >> n;
    int sum = 0;
    for (char c : n) {
        sum += (c-'0');
    }
    if(sum%9 == 0) cout << "Yes" << endl;
    else cout << "No" << endl;
}
