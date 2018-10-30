#include <iostream>
#include <cmath>

using namespace std;

int main() {
    const double pi = 3.141592653;
    int n = 10;
    double b = pi, a = 0, h, y = 0, s, sum = 0;
    h = b / n;
    for (a = 0; a < b; a += h) {
        y = a * sin(a);
        sum += y;
    }
    s = h * sum;
    cout << s;

    return 0;
}