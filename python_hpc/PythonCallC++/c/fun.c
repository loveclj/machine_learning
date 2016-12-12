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
#include<Python.h>

int fact(int n)
{
    long int sum = 0;
    for(int i = 0; i < n; ++i)
    {
        sum += i;
    }
    return sum;
}

PyObject *wrap_fact(PyObject *self, PyObject *args)
{
    int n , result;

    if(!PyArg_ParseTuple(args, "i:fact", &n))
    {
        return NULL;
    }

    result = fact(n);

    return Py_BuildValue("i", result);
}

static PyMethodDef exampleMethods[] =
{

    {"fact", wrap_fact, METH_VARARGS,"Caculate sum(N)!"},
    {NULL, NULL}
};

void initexample()
{
    PyObject *m;
    m = Py_InitModule("example", exampleMethods);
}

