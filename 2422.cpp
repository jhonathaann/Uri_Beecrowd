#include <iostream>

using namespace std;

int main(){
    int l, n;
    cin >> l >> n;

    long long int maior_tapete = l - n + 1;
    //                                                      quant de tapetes que sobrou"
    long long int resultado = maior_tapete * maior_tapete +  (n - 1);

    cout << resultado  << endl;
}