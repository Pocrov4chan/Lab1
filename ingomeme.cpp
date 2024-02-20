#include <iostream>

using namespace std;

int main() {
    long long a, b, c;
    while (cin >> a >> b >> c){
        while (b > 4){
            b /= 4;
        }
        long long res = 1;
        a = a % c;
        while(b > 0){
            if(b & 1){
                res = (res * a) % c;
            }
            a = (a * a) % c;
            b = b / 2;
        }
        cout << res << endl;
    }

    return 0;
}