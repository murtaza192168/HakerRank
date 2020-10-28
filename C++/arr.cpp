#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N,arr[N] ,i ;

    cin >> N;
    for(i=0;i<N;i++)
    {
        cin >> arr[i]; 
       
    }
    for(i=N;i>=0;i--)
    {cout << arr[i] << " ";
    }
    
    return 0;
}
