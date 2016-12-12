#!/usr/bin/env python
# coding=utf-8

"'compare list and map, list is an array, it's implamented by link, and map is hash table'"

from time import time 
t = time() 
list = ['a','b','is','python','jason','hello','hill','with','phone','test', 'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 
print list 
filter = [] 
for i in range (1000000): 
        for find in ['is','hat','new','list','old','.']: 
       	 if find not in list: 
       		 filter.append(find) 
print "total run time:"
print time()-t


list = dict.fromkeys(list,True) 
print list 
filter = [] 
t = time() 
for i in range (1000000): 
        for find in ['is','hat','new','list','old','.']: 
       	 if find not in list: 
       		 filter.append(find) 
print "total run time:"
print time()-t
