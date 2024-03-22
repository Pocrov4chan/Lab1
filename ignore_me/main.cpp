#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    int n, k, counter = 0;
    cin >> n >> k;
    int arr[n];
    for (int i = 0; i < n; ++i){
        cin >> arr[i];
    }

    sort(arr, arr + n);

    if (arr[n - 1] > k){
        cout << "Impossible";
        return 0;
    }

    for (int i = n - 1; i >= 0; --i){
        for (int j = i - 1; j >= 0; --j){
            if (arr[i] == 0 or arr[j] == 0){
                continue;
            }
            else if (arr[i] + arr[j] <= k){
                arr[i] = 0;
                arr[j] = 0;
                counter += 1;
            }
        }
    }
    for (int i = 0; i < n; i++){
        if (arr[i] != 0){
            counter += 1;
        }
    }
    cout << counter;
    return 0;
}