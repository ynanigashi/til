#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using P = pair<int, int>;

int main() {
    string s;
    cin >> s;
    if(s.at(s.size()-1) == 's') cout << s << "es" << endl;
    else cout << s << "s" << endl;
    return 0;
}
