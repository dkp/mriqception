#!/usr/bin/env python3

# Author: Dianne Patterson
# Purpose: To convert an mriqc output file to normalized scores for
# representation in a traffic-light table.

# import os
import numpy as np
import pandas as pd
import scipy.stats as stats
# import plotly.graph_objects as go


# pwd = os.getcwd()

# Argument is: 1) QA file
# Example:  norm_z.py group_T1w.tsv
# qa_file = sys.argv[1]
qa_file = "../../data/group_bold.tsv"
# print("qa_file is", qa_file)

qa_df = pd.read_csv(qa_file, sep="\t")
# print("qa_df is a:", type(qa_df))
# print(qa_df)

# try with the data frame itself:
z_df = qa_df.iloc[:, 1:].apply(stats.zscore)
# print("z_df is a:", type(z_df))
# print(z_df)

bids_names = qa_df['bids_name']
# print("bids_names is a:", type(bids_names))
# print(bids_names)

norm_df = pd.concat([bids_names, z_df], axis=1)
print(norm_df)
# print(norm_df[['aor', 'dummy_trs', 'fber', 'fd_num']])
