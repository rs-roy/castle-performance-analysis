#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:36:00 2023

@author: carolin
"""

import pandas as pd
import datetime as dt

def main():
    """
        input:
            1 dataset containing data of all clients, generated by merge_singleClients2OneSet.py
        procedure:
            split dataset to contain data of 1 year only
        output:
            1 dataset containing data of all clients per year
    """
    n_users = 370 # define number of users that shall be included in merged dataset, complete = 370 users
    data_path = "../consumption_data/"
    df = pd.read_csv((data_path + "merged_orig_consumption_" + str(n_users) + "_users.csv"), sep = ",", index_col = False)
    
    ### 2011
    min_date_str = "2011-01-01"
    max_date_str = "2012-01-01"
    min_date = dt.datetime.strptime(min_date_str, '%Y-%m-%d')
    max_date = dt.datetime.strptime(max_date_str, '%Y-%m-%d')
    
    df_split = df.loc[((pd.to_datetime(df["date"]) >= min_date) & (pd.to_datetime(df["date"]) < max_date))]
    df_split.to_csv((data_path + "2011_consumption.csv"), sep = ",", index = False)
    
    ### 2012
    min_date_str = "2012-01-01"
    max_date_str = "2013-01-01"
    min_date = dt.datetime.strptime(min_date_str, '%Y-%m-%d')
    max_date = dt.datetime.strptime(max_date_str, '%Y-%m-%d')

    df_split = df.loc[((pd.to_datetime(df["date"]) >= min_date) & (pd.to_datetime(df["date"]) < max_date))]
    df_split.to_csv((data_path + "2012_consumption.csv"), sep = ",", index = False)
    
    ### 2013
    min_date_str = "2013-01-01"
    max_date_str = "2014-01-01"
    min_date = dt.datetime.strptime(min_date_str, '%Y-%m-%d')
    max_date = dt.datetime.strptime(max_date_str, '%Y-%m-%d')

    df_split = df.loc[((pd.to_datetime(df["date"]) >= min_date) & (pd.to_datetime(df["date"]) < max_date))]
    df_split.to_csv((data_path + "2013_consumption.csv"), sep = ",", index = False)
    
    ### 2014 + 1.1.2015
    min_date_str = "2014-01-01"
    max_date_str = "2015-01-02"
    min_date = dt.datetime.strptime(min_date_str, '%Y-%m-%d')
    max_date = dt.datetime.strptime(max_date_str, '%Y-%m-%d')

    df_split = df.loc[((pd.to_datetime(df["date"]) >= min_date) & (pd.to_datetime(df["date"]) < max_date))]
    df_split.to_csv((data_path + "2014_consumption.csv"), sep = ",", index = False)
    
if __name__ == "__main__":
    main()