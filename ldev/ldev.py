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
'''
read_csv
read_excel
read_hdf
read_sql
read_json
read_msgpack (experimental)
read_html
read_gbq (experimental)
read_stata
read_sas
read_clipboard
read_pickle
'''
# Laod data
def load(filename,extension):
    if extension == 'csv':
        df = pd.read_csv(filename)
    if extension == 'hdf':
        df = pd.read_hdf(filename)
    if extension == 'xlsx' or extension == 'xlsx':
        df = pd.read_excel(filename,'Sheet1')
    if extension == 'sas':
        df = pd.read_sas(filename)
    if extension == 'sql':
        #df = pd.read_sql_query('')
        pass
    if extension == 'json':
        pass
    if extension == 'html':
        pass
    if extension == 'stata':
        pass
    if extension == 'sas':
        pass
    if extension == 'gbq':
        pass
    if extension == 'pickle':
        pass
    if extension == 'msgpack':
        pass
    if extension == 'clipbaord':
        pass
    return df
    
    
#-----descriptive statistics----
def diagnose():
    pass

def explore():
    pass
#----end of descritive---------

def visualize():
    pass



if __name__ == '__main__':main()


