/*************************************************************************
	> File Name: mpicc.cpp
	> Author:lizhifeng 
	> Mail:lizhifeng2009@126.com 
	> Created Time: 2015年09月16日 星期三 11时09分06秒
 ************************************************************************/

#include<iostream>
#include<string>
#include"mpi.h"
#include<sys/time.h>

using namespace std;

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int m = 1000000;
    
    int *arr = new int[m];

    for(int i= 0 ; i < m ; i++)
    {
        arr[i] = i;
    }
    int *result = new int[m];

    struct timeval timerStart, timerStop, timerElapsed;
    gettimeofday(&timerStart, NULL);
    MPI_Reduce(arr, result, m, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    cout << result[1000] << endl;
    cout << arr[1000] << endl;
    
    gettimeofday(&timerStop, NULL);
    timersub(&timerStop, &timerStart, &timerElapsed);
    cout << timerElapsed.tv_sec *1000000 + timerElapsed.tv_usec << endl;

    delete [] arr;
    delete [] result;
    MPI_Finalize();


    return 0;
}
