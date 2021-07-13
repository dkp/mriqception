#!/usr/bin/env python3

# Author: Dianne Patterson
# Purpose: To convert an mriqc output file to normalized scores for
# representation in a traffic-light table.

# import os
from matplotlib import cm
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd
import scipy.stats as stats

# import plotly.graph_objects as go


# pwd = os.getcwd()

# Argument is: 1) QA file
# Example:  norm_z.py group_T1w.tsv
# qa_file = sys.argv[1]
qa_file = "../../data/gtest.tsv"
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

# create our own limited color map
radish9 = cm.get_cmap('PiYG', 9)

# set cell backgrounds based on data and our colormap
# Note: unfortunately can't set discrete intervals or
# center the colormap on zero.
# norm_df.style.background_gradient(cmap=radish9, axis=None)

# plt.imshow([[0, 1, 2, 3, 4, 5, 6, 7, 8]], cmap=radish9)
plt.imshow(z_df, cmap=radish9)
plt.show()