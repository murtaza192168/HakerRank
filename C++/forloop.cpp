#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    

    int a , b , n;
   
    string c[] = {"","one","two","three","four","five","six","seven","eight","nine"};
     cin >> a >> b;

    for(n=a;n<=b;n++)
    {
        cout << ((n<=9)?c[n]:((n%2==0)?"even":"odd")) << endl; /*Ternary Operator*/
    }
    return 0;
}
