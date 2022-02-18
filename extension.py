# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:59:38 2022

@author: HTM
"""

filename = input("Input the Filename: ")
f_ext = filename.split(".")
print ("The extension of the file is : " + repr(f_ext[-1]))