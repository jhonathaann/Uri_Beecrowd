#include <iostream>

using namespace std;

int main(){
    int e, d;

    cin >> e;
    cin >> d;

    if(e > d){
        cout << e+d << endl;
    }else{
        cout << 2 * (d-e) << endl;
    }

    return 0;
}