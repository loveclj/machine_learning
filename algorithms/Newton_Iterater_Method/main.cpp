#include <iostream>
#include <math.h>

using namespace std;

float newton_sqrt(float v, float EPS = 0.00001)
{
    if(v <= 0) return 0;

    float  x;
    float  x_next;
    x  = 10;
    while(1)
    {
        x_next = (x + v/x)/2;
        float diff = x_next - x;
        if(diff < EPS && diff > -EPS)
        {
            return x_next;
        }
        else
        {
            x = x_next;
        }

    }
}
int main() {

    float test_value = 20;

    float newton_sqrt_result = newton_sqrt(test_value);
    float math_sqrt_result   = sqrtf(test_value);

    cout << " Newton iterater method: " << newton_sqrt_result << endl;
    cout << " math Library methon: " << math_sqrt_result << endl;
    return 0;
}