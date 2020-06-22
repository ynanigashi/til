#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string S;
    cin >> S;
    int A = 1;
    for (int i = 1; i < S.size(); i += 2){
        if (S.at(i) == '+'){
            A += 1;
        } else {
            A -= 1;
        }
    }
    cout << A << endl;
}
