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
    vector<string> t(4);
    t.at(0) = "dream";
    t.at(1) = "dreamer";
    t.at(2) = "erase";
    t.at(3) = "eraser";

    int i = s.size();
    while (i > 1) {
        bool same_flg = false;
        for(string word : t){
            int n = word.size();
            if(i < n) continue;
            if(s.substr(i - n, n) == word) {
                i -= n;
                same_flg = true;
                break;
            }
        }
        if(!same_flg){
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
    return 0;
}