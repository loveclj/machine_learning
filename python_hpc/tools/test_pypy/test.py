import time

def test(n,m):
    m=m
    vals = []
    keys = []
    for i in xrange(m):
        vals.append(i)
        keys.append('a%s'%i)
    d = None
    for i in xrange(n):
        d = dict(zip(keys, vals))
    return d
if __name__ == '__main__':
    st = time.time()
    print test(1000000,100)
    print 'use:', time.time() - st
