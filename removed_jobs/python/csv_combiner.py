# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:29:29 2019

@author: Zac
"""

import os
import glob
import pandas as pd
os.chdir(r"/home/benemenadmin/Desktop/lt")
extension = 'csv'
all_filenames = [i for i  in glob.glob('*.{}'.format(extension))]


combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')