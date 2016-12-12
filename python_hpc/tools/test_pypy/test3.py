from time import time 
def test(n): 
       a =0; 
       for i in xrange(n): 
               a+= i 
       return a 

t = time() 
test(10000000) 
print "total run time:"
print time()-t 
