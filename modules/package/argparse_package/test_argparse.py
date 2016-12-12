__author__ = 'lizhifeng'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", help ="version")
parser.add_argument("--s", help = "default value", default="123")
parser.add_argument("-i", help = "set int", type = int, default=22)
parser.add_argument("-t", help = "can't pass value", action = "store_true") #if action is set as store_true, -t can't set value, if
args =parser.parse_args()                                                   # command line show as -t value, it's forbbiden

print args.v
print args.t
print args.s
print args.i
print type(args.i)


