#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

ll sum(int n){
    if(n == 0 ) return 0;

    return n + sum(n-1);
}

int sum_range(int a, int b) {
    if (a == b) return a;

    return a + sum_range(a+1, b);
}

ll factorial(int n) {
    if(n == 1) return 1;

    return n * factorial(n-1);
}

int sum_vector(vector<int> &data, int i){
    if(i == data.size()) return 0;

    return data.at(i) + sum_vector(data, i+1);

}


int main() {
    cout << sum(100) << endl;
    cout << sum_range(5, 8) << endl;
    cout << factorial(10) << endl;
    int N = 101;
    vector<int> int_list(N);
    rep(i, N) int_list.at(i) = i;
    cout << sum_vector(int_list, 1) << endl;

}
