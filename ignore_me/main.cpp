#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int INF = 1e9;
vector<int> coins = {1, 3, 4};
vector<int> value(1000, INF);
vector<bool> ready(1000, false); 

int solve(int x) {
    if (x < 0) return INF;
    if (x == 0) return 0;
    if (ready[x]) return value[x];
    int best = INF;
    for (auto c : coins) {
        best = min(best, solve(x - c) + 1);
    }
    value[x] = best;
    ready[x] = true;
    return best;
}

int main() {
    int sum = 10;
    cout << solve(sum) << endl;
    return 0;
}
