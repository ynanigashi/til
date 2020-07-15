#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vivi = vector<vi>;

int main() {
    int n;
    cin >> n;
    vector<P> P_list(n);
    rep(i, n){
        P p;
        cin >> p.second;
        cin >> p.first;
        P_list.at(i) = p;
    }
    sort(P_list.begin(), P_list.end());
    for(auto p: P_list){
        cout << p.second << " " << p.first << endl;
    }
}
