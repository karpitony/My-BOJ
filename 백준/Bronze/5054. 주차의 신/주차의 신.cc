#include <stdio.h>
#include <iostream>

using namespace std;


int main() {

    int t;
    cin >> t;
    for (int i=0; i<t; i++) {

        int n;
        cin >> n;
        int result, min = 100, max = 0;
        
        for (int k=0; k<n; k++) {
            int input;
            cin >> input;
            if (input > max) max = input;
            if (input < min) min = input;
        }

        result = (max - min) * 2;
        cout << result << '\n';
    }

}