#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int N;
    cin >> N;
    vector<int> cnt_list(N+1);
    for(int X = 1; X <= 100; X++) {
        for(int Y = 1; Y <= 100; Y++){
            for(int Z = 1; Z <= 100; Z++){
                int s = X*X + Y*Y + Z*Z + X*Y + Y*Z + Z*X;
                if(s <= N) cnt_list[s]++; 
            }
        }
    }
    for (int i = 1; i <= N; i++){
        cout << cnt_list[i] << endl;
    }
}
