#include <iostream>
#include <vector>

using namespace std;

int count(vector <pair <int, int>> array, int endpoint, int stage, int sum){
  if (stage == endpoint){
    return sum % 2;
  }

  int branch_1 = count(array, endpoint, stage + 1, sum + array[stage].first);
  int branch_2 = count(array, endpoint, stage + 1, sum + array[stage].second);

  return branch_1 + branch_2;
}

int main(){
  
}