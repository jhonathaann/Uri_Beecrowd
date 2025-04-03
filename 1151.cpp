#include <iostream>

using namespace std;

int main(){
    int n, fib0 = 0, fib1 = 1, fib;

    cin >> n;

    for(int i = 0; i < n; i++){

        if(i > 0)
            cout << " ";
        cout << fib0;
        fib = fib0 + fib1;
        fib0 = fib1;
        fib1 = fib;
    }

    cout << endl;

    return 0;
}