#include <iostream>

using namespace std;

int main()
{
    int d, a, l, p;
    
    // lendo as variaveis
    cin >> d;
    cin >> a >> l >> p;
    
    if(a >= d && l >= d && p >= d){
        cout << "S" << endl;
    }else{
        cout << "N" << endl;
    }
    
    return 0;
}