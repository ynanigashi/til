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
    vvi a(n + 1, vector<int>(3));
    for(int i = 1; i <= n; i++){
        int t, x, y;
        cin >> t >> x >> y;
        a.at(i).at(0) = t;
        a.at(i).at(1) = x;
        a.at(i).at(2) = y;
        int preb, turn, d;
        preb = i - 1;
        turn = t - a.at(preb).at(0);
        d = abs(x - a.at(preb).at(1)) + abs(y - a.at(preb).at(2));
        if(d <= turn && (turn - d)%2 == 0) continue;
        else{
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}