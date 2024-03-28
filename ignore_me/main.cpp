#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    int arr[n];

    for (int i = 0 ; i < n; ++i){
        cin >> arr[i]; 
    }

    sort(arr, arr + n);

    if(arr[n - 1] > k){
        cout << "Impossible";
        return 0;
    }

    int left_side = 0;
    int right_side = n - 1;
    int counter = 0;

    while(left_side <= right_side){
        if(arr[left_side] + arr[right_side] > k){
            right_side -= 1;
            counter += 1;
        }
        else{
            right_side -= 1;
            left_side += 1;
            counter += 1;
        }
    }
    cout << counter;



}