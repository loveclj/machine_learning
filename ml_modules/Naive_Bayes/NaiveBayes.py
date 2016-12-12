#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: NaiveBayes.py
@time: 11/9/16 4:57 PM
"""
import LoadData
from collections import defaultdict
import pandas as pd
import numpy as np

if __name__ == '__main__':

    data_file_name = "../data/SMSSPamColloction"
    data = LoadData.load_spam_data(data_file_name)

    word_count = defaultdict(int)
    label_count = defaultdict(int)

    for item in data:
        label_count[item[0]] += 1
        # print item
        for w in item[1]:
            word_count[w] += 1

    df = pd.DataFrame(np.zeros(shape=[len(label_count), len(word_count)]), columns=word_count.keys() )
    for item in data:
        row = 0
        if item[0] == 'spam':
            row = 1

        for w in item[1]:
            df[w][row] += 1


# 采用拉普拉斯平滑
    lam = 1
    K = 2  # 分类数目
    S = 2
    for w in word_count.keys():
        N = df[w][0] + df[w][1] + S * lam
        df[w][0] = (df[w][0] + lam) / N
        df[w][1] = (df[w][1] + lam) / N



    spam_prob = float(label_count["spam"])/ (label_count["ham"] + label_count["spam"])
    pam_prob = 1 - spam_prob

    # print spam_prob
    # print pam_prob


    test = [ 'free', 'credit', 'valid', 'call']

    test_spam_prob = spam_prob
    test_pam_prob = pam_prob

    for w in test:
        if w not in word_count.keys():
            print "not in"
            continue

        test_pam_prob *= df[w][0]
        test_spam_prob *= df[w][1]

    print test_pam_prob
    print test_spam_prob


    # print df
    # # print df['yellow']
    # print label_count
    # print len(word_count)



