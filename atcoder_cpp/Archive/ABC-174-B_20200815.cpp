#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    int n; 
    set<int> l;
    rep(i, n) {
        int j;
        cin >> j;
        l.insert(j);
    }
    int ans = 0;
    for (auto i : l){
        for (auto j : l){
            if(i == j) continue;
            for (auto k : l){
                if(i == k) continue;
                if(j == k) continue;
                if(max({i, j, k}) == i) { if(abs(j-k) < i && i < j+k) ans++; }
                if(max({i, j, k}) == j) { if(abs(i-k) < j && j < i+k) ans++; }
                if(max({i, j, k}) == k) { if(abs(j-i) < k && k < j+i) ans++; }
            }
        }
    }
    cout << ans << endl;

}
