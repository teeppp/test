# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:10:13 2017
original Lib Module
@author: T
"""

import sys
import os
import numpy as np

def Get_Pathlists(root_dir):
    file_list = []
    path_list = []

    for root, dirs, files in os.walk(root_dir):
        for fileo in files:
            print("-----------------------")
            fulpath = root + "\\" + fileo
            path_list = np.append(path_list,fulpath)
            file_list = np.append(file_list,fileo)
    
    
    print("<result>")
    print("-----------------------")
    print(path_list)
    print(file_list)
    return([path_list, file_list])
