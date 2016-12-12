/*************************************************************************
	> File Name: test3.cpp
	> Author:lizhifeng 
	> Mail:lizhifeng2009@126.com 
	> Created Time: 2015年09月15日 星期二 11时33分54秒
 ************************************************************************/

#include<iostream>
#include<string>
#include<sys/time.h>

using namespace std;

int main(int argc, char **argv)
{
    struct timeval timerStart, 
                   timerStop,
                   timerElapsed;

    gettimeofday(&timerStart, NULL);
    const long int N = 10000000;
    long int sum     = 0;

    for(int i = 0; i< N;)
    {
        sum += ++i;
        sum += ++i;
        sum += ++i;
        sum += ++i;
        sum += ++i;
        sum += ++i;
        sum += ++i;
        sum += ++i;
    }

    gettimeofday(&timerStop, NULL);
    timersub(&timerStop, &timerStart, &timerElapsed);

    cout << sum << endl;
    cout << timerElapsed.tv_sec *1000000 + timerElapsed.tv_usec <<" us" << endl;
    return 0;
}
