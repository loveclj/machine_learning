/*************************************************************************
	> File Name: sum.cpp
	> Author:lizhifeng 
	> Mail:lizhifeng2009@126.com 
	> Created Time: 2015年09月14日 星期一 17时34分09秒
 ************************************************************************/

#include<iostream>
#include<string>
#include<sys/time.h>

using namespace std;

const  int N = 1000;
const  int LOOP = 10000;
int main(int argc, char **argv)
{
    struct timeval timerStart, timerStop, timerElapsed;
    gettimeofday(&timerStart, NULL);
    int *sums = new int[LOOP];

    int *arr = new int [N];
    for(int i = 0; i < LOOP; ++i)
    {
        for(int j = 0; j < N; ++j)
        {
            arr[j] = j;
        }
        int sum = 0;
        for(int j =0; j < N; ++j)
        {
            int tmp = arr[j];
            sum += tmp * tmp;
        }
        sums[i] = sum;
    }
    delete [] arr;

    gettimeofday(&timerStop, NULL);
    timersub(&timerStop, &timerStart, &timerElapsed);
    cout << "time elapsed is " <<  (float)timerElapsed.tv_sec * 1000 + (float)timerElapsed.tv_usec/1000 << " ms" << endl;

    int ret = sums[0];
    delete []sums;
    return 0;
}
