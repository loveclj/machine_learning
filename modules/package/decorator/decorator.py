__author__ = 'lizhifeng'

def decorator_fun(func):
    def _deco():
        print "decorator fun begin"
        func()
        print "decorator fun end"

    return  _deco


@decorator_fun
def func():
    print "fun excute"


func()

