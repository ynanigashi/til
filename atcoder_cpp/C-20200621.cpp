#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
 
int main() {
    long long N;
    cin >> N;
    string name_str;
    while (N > 0){
        N -= 1;
        name_str +=  'a' + N%26;
        N /= 26;
    }
    reverse(name_str.begin(), name_str.end());
    cout << name_str << endl;
}