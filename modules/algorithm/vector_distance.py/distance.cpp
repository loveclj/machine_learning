/*************************************************************************
	> File Name: distance.cpp
	> Author:lizhifeng 
	> Mail:lizhifeng2009@126.com 
	> Created Time: 2015年09月14日 星期一 16时42分35秒
 ************************************************************************/

#include<iostream>
#include<string>
#include<stdlib.h>
#include<sys/time.h>

using namespace std;

int main(int argc, char **argv)
{
    const int dimenssion = 500000;
    float *vec1 = new float[dimenssion];
    float *vec2 = new float[dimenssion];

    srand(1);
    
    for(int i = 0; i < dimenssion; i++)
    {
        vec1[i] = (float)(rand()&0x8FFF)/0x8FFF;
        vec2[i] = (float)(rand()&0x8FFF)/0x8FFF;
    }

    float sum = 0;
    struct timeval timerStop, timerStart;
    gettimeofday(&timerStart, NULL);
    for(int i = 0; i < dimenssion; ++i)
    {
 //       cout << vec1[i] << endl;
        float diff = vec1[i] - vec2[i];
        sum += diff * diff;
    }

    gettimeofday(&timerStop, NULL);

    cout << "sum is " << sum << endl;
    struct timeval diff;
    timersub(&timerStop, &timerStart,  &diff);
    cout << "time elaspsed: " << diff.tv_sec *1000000 + diff.tv_usec << " us" << endl;

    return 0;
}
