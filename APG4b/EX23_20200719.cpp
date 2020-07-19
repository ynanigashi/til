#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    int n;
    cin >> n;
    map<int, int> am;
    int max_num = 0;
    am[max_num];
    rep(i, n){
        int a;
        cin >> a;
        am[a]++;
        if(am.at(max_num) < am.at(a)) max_num = a;
    }
    cout << max_num << " " << am.at(max_num) << endl;
}
