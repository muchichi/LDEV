#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

"""
Created on Thu Apr 27 20:06:54 2017

@author: mussie

Common data problems
    - Inconsistent column names
    - Missing Data
    - Outliers
    - Duplicate rows
    - Untidy (transformation issue)
    - Need to process columns
    - Column types can signal unexpected data values
"""

def main():
    pass

# Laod data
def load(filename,extension):
    if extension == 'csv':
        df = pd.read_csv(filename)
    if extension == 'hdf':
        df = pd.read_hdf(filename)
    if extension == 'xlsx' or extension == 'xlsx':
        df = pd.read_excel(filename)
    if extension == 'sas':
        df = pd.read_sas(filename)        
    return df
    pass
#-----descriptive statistics----
def diagnose():
    pass

def explore():
    pass
#----end of descritive---------

def visualize():
    pass



if __name__ == '__main__':main()


