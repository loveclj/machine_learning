import  commands
import re

def listdir(dir):
    cmd = "ls %s" %dir
    status, output =  commands.getstatusoutput(cmd)
    return output.split()

fileList = listdir(("./"))
print fileList

compiler_cmd  = "mpic++ -g -fopenmp "
compiler_flag = "-I../googletest/include\
 -I../../src -I../../src/rapidjson -L../googletest -I../../src/mrmpi \
 -I../../src/util -L../../build/src -lmmsom  -lgtest -lpthread\
  -lPocoUtil -lPocoNet -lPocoXML -lPocoNetSSL -lPocoFoundation \
   -lmongoclient -lboost_thread -lboost_regex  -lboost_program_options\
    -lboost_filesystem -lboost_system  -L../../build/src/mrmpi -lmrmpi "

print compiler_cmd
regex = "test"
for file in fileList:
    if re.search(regex, file):
        print file
        arr = file.split(".")
        print arr
    else:
        print "not search"




