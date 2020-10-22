#include <iostream>
#include <cstdio>
#include<iomanip>
using namespace std;

int main() {
    // Complete the code.
    int a;
    long b;
    char c;
    float f;
    double d;
    scanf("%d %ld %c",&a,&b,&c);
    printf("%d\n%ld\n%c\n",a,b,c);
    cin >> f;
    cout<<fixed<<setprecision(3)<<f<<endl;
    cin>>d;
    cout<<fixed<<setprecision(9)<<d<<endl;

    return 0;
}
