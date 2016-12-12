/*************************************************************************
	> File Name: fun.c
	> Author:lizhifeng 
	> Mail:lizhifeng2009@126.com 
	> Created Time: 2015年10月19日 星期一 11时01分05秒
 ************************************************************************/

#include<stdio.h>
#include<unistd.h>
#include<string.h>
#include<stdlib.h>

int fact(int n)
{
    long int sum = 0;
    for(int i = 0; i < n; ++i)
    {
        sum += i;
    }
    return sum;
}

int main(int argc, char **argv)
{
    int n = *((int*)argv[1]);

    long int sum = 0;

    sum = fact(n);
    printf("sum is %ld\n", sum);
    
}
