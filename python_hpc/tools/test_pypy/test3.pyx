from time import time 
def test(int n): 
       t = time() 
       cdef int a =0 
       cdef int i 
       for i in xrange(n): 
               a+= i 
       print "total run time:"
       print time()-t
       return a 

test(10000000) 
