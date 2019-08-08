# Welcome to mriqception!

- [Introduction](#introduction)
  * [Why mriqception exists](#why-mriqception-exists)
    + [Why is this useful?](#why-is-this-useful-)
  * [What mriqception does](#what-mriqception-does)
    + [What mriqception does NOT do](#what-mriqception-does-not-do)
- [How to use mriqception](#how-to-use-mriqception)
  * [Requirements](#requirements)
  * [Functions](#functions)
- [Resources](#resources)

# Introduction

## Why mriqception exists

The goal for this Neurohackademy 2019 project is to provide context for the image quality metrics (IQMs) shown in the <a href="https://github.com/poldracklab/mriqc">MRIQC group reports</a>, by showing the distribution of IQMs for your data plotted relative to a larger set of anonymized IQMs pulled from the <a href="https://www.biorxiv.org/content/10.1101/216671v1">web API</a>.

### Why is this useful?
As described in the MRIQC documentation, many of the IQMs calculated are "no-reference" metrics. "A no-reference IQM is a measurement of some aspect of the actual image which cannot be compared to a reference value for the metric since there is no ground-truth about what this number should be." [[link]](https://mriqc.readthedocs.io/en/stable/measures.html) Therefore, it can be difficult for users to get a sense of how their data quality compares to normative data quality.

For example, in this dataset it's easy to see that there's one participant whose mean framewise displacement is much greater than the rest.

![first example: obvious outlier on boxplot](https://github.com/sarenseeley/mriqception/blob/master/docs/wikiplot1.png)


But in the dataset shown below, there are no obvious outliers. However, note that _everyone_ in this sample has an undesirably high degree of motion (mean FD >2mm!)

![second example: no obvious outliers on boxplot, but everyone's mean FD is >2mm](https://github.com/sarenseeley/mriqception/blob/master/docs/wikiplot2.png)

Hopefully, you're actually paying attention to the Y-axis scale, but we designed mriqception to make it easier to quickly spot problems like this. The plot below shows these first two example datasets relative to 10,000 datapoints from the web API:

![third example: the first two plots shown relative to 10k other simulated datapoints. the second example is obviously at the upper part of the ](https://github.com/sarenseeley/mriqception/blob/master/docs/wikiplot3.png)

From this figure, you can immediately see that the second example dataset falls significantly outside of the web API data median and quartiles, indicating overall poor quality data.

## What mriqception does

mriqception takes user IQMs from MRIQC and plots them relative to IQMs pulled from the 200k+ images in MRIQC web API (we're going to call those  "normative" IQMs). The user has the option to filter their API query by relevant acquisition parameters, such as TR/TE.

mriqception also features a brief description of the IQM, shown as a tooltip when you mouseover the name of the IQM. We have tried to make these descriptions as user-friendly as possible.


### What mriqception does NOT do

Like <a href="https://github.com/poldracklab/mriqc">MRIQC</a>, mriqception is descriptive rather than prescriptive.

Importantly, mriqception does not tell you whether your IQMs are "good" or not. It simply shows you how the IQMs from your sample compare to other users' data, as an additional decision-making tool for your QC process and as a way to quickly compare how image quality in your dataset compares to other datasets. What you do with that information is up to you!

# How to use mriqception

1.
2.
3.
4.
5.
6.

## Requirements

1. You must have run <a href="https://github.com/poldracklab/mriqc">MRIQC</a> on your data least at the group level, and generated group .TSV files for each modality (T1w, T2w, BOLD) you want to look at. These are named something like `group_t1w.tsv` and/or `group_bold.tsv`, and should be located in `/<PATH TO YOUR BIDS DIRECTORY>/derivatives/mriqc/`
2. < ADD OTHER REQUIREMENTS HERE >
3. < ADD OTHER REQUIREMENTS HERE >

## Functions

< ADD FUNCTIONS USED, W/EXPLANATIONS, HERE >

# Resources

* <a href="https://github.com/poldracklab/mriqc">MRIQC</a>
* <a href="https://mriqc.readthedocs.io/en/stable/">MRIQC documentation</a>
* <a href="https://github.com/neurohackademy/2019_projects">Neurohackademy 2019 projects repo</a>
