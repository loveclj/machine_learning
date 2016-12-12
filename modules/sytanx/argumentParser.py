#!/usr/bin/env python
# coding=utf-8
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s")
parser.add_argument("-c")

args = parser.parse_args()

print args.s
print args.c

#execute like this: python argparse.py -s 1 -c tt
