#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int complete_time(vector<vector<int>> &children, int x){
    if( children.at(x).size() == 0 ) return 0;
    int max_time = 0;
    for(int i: children.at(x)){
        int temp_time = complete_time(children, i) + 1;
        max_time = max(max_time, temp_time);
    }
    return max_time;
}

int main() {
    int N;
    cin >> N;
    vector<int> P(N);
    P.at(0) = -1;
    for (int i = 1; i < N; i++){
        cin >> P.at(i);
    }
    
    vector<vector<int>> children(N);
    for (int i = 1; i < N; i++){
        children.at(P.at(i)).push_back(i);
    }

    cout << complete_time(children, 0) << endl;
}
