#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int A, B;
    string op, er;
    er = "error";
    cin >> A >> op >> B;
    if (op == "+" ){
        cout << A + B << endl;
    } else if (op == "-"){
        cout << A - B << endl; 
    } else if (op == "*"){
        cout << A * B << endl;
    } else if (op == "/"){
        if (B == 0){
            cout << er << endl;
        } else {
            cout << A / B << endl;
        }
    } else {
        cout << er << endl;
    }
}