#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, A;
    cin >> N >> A;
    for (int i = 1; i <= N; i++){
        string op;
        int B;
        cin >> op >> B;
        if (op == "+"){
            A += B;
        } else if (op == "-"){
            A -= B;
        } else if (op == "*"){
            A *= B;
        } else {
            if(B == 0){
                cout << "error" << endl;
                break;
            }
            A /= B;
        }
        cout << i << ":" << A << endl;
    }
}
