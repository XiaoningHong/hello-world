#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:10:16 2020

@author: hongxiaoning
"""

Usage="""
This script 
Usage:
    python temp.py inputfile1 outputname
"""
    
import gzip
import re
import os
from sys import argv
from collections import defaultdict

def parser(inputfile,outputfile):
    if inputfile.endswith(".gz") == False:
        File = open(inputfile,'r')
    else:
        File = gzip.open(inputfile,'rt')
        
    dict_stat = defaultdict(int)
    for line in File:
        line = line.strip()
        if line.startswith("#") == False:
                           line = re.split("\s+",line)
                           dict_stat[line[0]] += 1
    return(dict_stat)
    
if __name__ == "__mian__":
    if len(argv) < 2:
        print (Usage)
    else:
        parser(argv[1],argv[2])
        
        
        
