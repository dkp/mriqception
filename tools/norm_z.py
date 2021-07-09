#!/usr/bin/env python3

# Author: Dianne Patterson
# Purpose: To convert an mriqc output file to normalized scores for
# representation in a traffic-light table.

# import argparse
# import os
import numpy as np
import pandas as pd
import scipy.stats as stats
import sys

# pwd = os.getcwd()

# Argument is: 1) qa file
# Example:  z.py group_T1w.tsv
qa_file = sys.argv[1]

# print("qa_file is", qa_file)

qa=pd.read_csv(qa_file,sep="\t")
print("qa is a:", type(qa))

# print(qa)

# stats=qa[["cjv", "cnr", "efc"]].describe()
# describe all of the columns
stats=qa.describe()
# print(stats)
# convert it to numpy array (unfortunately, it still has the first column)
qa_matrix=qa.to_numpy()
print("qa_matrix is a", type(qa_matrix))
print(qa_matrix)
print ("====================")
# print all rows, columns 1 to the end (0-indexing) 
qa_matrix2=qa_matrix[:,1::]
print("qa_matrix2 is a", type(qa_matrix2))
print(qa_matrix2)
print ("====================")
stats.zscore([qa_matrix2])
print(z)

# Hmmm problems with datatypes
# Traceback (most recent call last):
#   File "/Volumes/Main/Working/Plante_BIDS_QA/code/z.py", line 46, in <module>
#     stats.zscore(qa_matrix2)
#   File "/Users/dpat/opt/miniconda3/envs/tables/lib/python3.8/site-packages/pandas/core/generic.py", line 5465, in __getattr__
#     return object.__getattribute__(self, name)
# AttributeError: 'DataFrame' object has no attribute 'zscore'

# The following works because there are no strings??
#data = np.array([6, 7, 7, 12, 13, 13, 15, 16, 19, 22])
#norm=stats.zscore(data)
#print(norm)
#stats.zscore(qa, axis=1, nan_policy='omit')
