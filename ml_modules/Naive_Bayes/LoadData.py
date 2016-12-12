#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: LoadData.py
@time: 11/9/16 4:30 PM
"""


import re
import string
from nltk.stem import WordNetLemmatizer


def load_spam_data(file_name):

    data = []
    lemm = WordNetLemmatizer()
    for line in open(file_name):
        words = re.split(' |\t', line.strip('\n').translate(None, string.punctuation))

        if len(words) < 2:
            continue

        kv = (words[0], set())


        for w in words[1:]:

            try:

                w = lemm.lemmatize(w)
            except:
                continue
            if len(w) < 4:
                continue

            kv[1].add(w.lower())

        # print kv
        data.append(kv)

    return data


if __name__ == '__main__':

    print load_spam_data("../data/SMSSPamColloction")