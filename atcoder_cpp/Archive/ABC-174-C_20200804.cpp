#include <bits/stdc++.h>
using namespace std;

int main() {
    int k;
    cin >> k;
    int x = 7%k;
    set<int> s;
    int i = 1;
    if (k%2 == 0 || k%5 == 0 ) {
        cout << -1 << endl;
        return 0;
    }
    while (s.count(x) == 0) {
        if(x == 0) {
            cout << i << endl;
            return 0;
        }
        s.insert(x);
        x = (x*10+7)%k;
        i++;
    }
    cout << -1 << endl;
    return 0;
}