#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

int main() {
    int a, b;
    cin >> a >> b;
    if((a * b)%2 == 0) cout << "Even" << endl;
    else cout << "Odd" << endl;
    return 0;
}
