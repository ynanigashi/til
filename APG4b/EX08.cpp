#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int flg, p, N;
    string txt;
    cin >> flg;
    if (flg == 2){ cin >> txt;}
    cin >> p >> N;
    if (flg == 2){ cout << txt + "!" << endl; }
        cout << p * N << endl;
}