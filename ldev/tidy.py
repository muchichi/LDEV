#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:34:34 2017

@author: mussie
"""
'''
Principles of tidy data:
    - Columns represent separeate variables
    - Rows represent individual observations
    - Oveservational units form tables
    
    ** Data for REPORTING V ANALYSIS
'''


def tidy():
    pass
#
def melt():
    pass
'''
Turn columns into rows, i.e. turn unique values into separate columns
We do this when:
    Reshape data from ANALYSIS friendly to REPORTING friendly shape
    Violates tidy data principles: If rows contain observations(multiple variables stored in the same column)
'''
def pivot():
    pass

#When duplicate values can't be pivoted, so we use aggfunc param in pivot_table()
def pivottable():
    pass

def split_column(separator):
    pass

def get_create_column(column,index):
    pass


if __name__ == '__main__': tidy()