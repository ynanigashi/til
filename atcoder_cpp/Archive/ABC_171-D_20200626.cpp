#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int N;
    cin >> N;
    //vector<int> A;
    int MX = 100001;
    vector<int> int_list(MX);
    ll sum = 0;
    rep(i, N){
        int a;
        cin >> a; 
      //  A.at(i) = a;
        int_list.at(a) += 1;
        sum += a; 
    }
    int Q;
    cin >> Q;
    rep(i, Q){
        int B, C;
        cin >> B >> C;
        sum += (C-B) * int_list.at(B);
        cout << sum << endl;
        int_list.at(C) += int_list.at(B);
        int_list.at(B) = 0;
    }
}
