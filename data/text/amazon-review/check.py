#!/usr/bin/env python
# Created by "Thieu" at 17:43, 26/11/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

## There is 5 files csv that was splitted by test file in this kaggle link:
## https://www.kaggle.com/code/vishalpatil123456/amazon-review-sentimental-analysis

## Train file is too big, test file is also too big. Can't put it in Github.
## So I split the test file to 5 files csv.


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import bz2 # To open zipped files
import re # regular expressions
import os
import gc

import matplotlib.pyplot as plt
import seaborn as sns

test_file = bz2.BZ2File('test.ft.txt.bz2')
test_file_lines = test_file.readlines()

del test_file
gc.collect()

test_file_lines = [x.decode('utf-8') for x in test_file_lines]

test_labels = [0 if x.split(' ')[0] == '__label__1' else 1 for x in test_file_lines]

test_sentences = [x.split(' ', 1)[1][:-1] for x in test_file_lines]


print(test_sentences[0])
print(test_labels[0])
n_items = 80000

for idx in range(1, 6):
    id1 = (idx-1)*n_items
    id2 = idx*n_items
    df = pd.DataFrame(list(zip(test_labels[id1:id2], test_sentences[id1:id2])), columns =['label', 'text'])
    df.to_csv(f"data_{idx}.csv", index=False)

