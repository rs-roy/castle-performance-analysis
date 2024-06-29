#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:54:59 2023

@author: carolin
"""

import pandas as pd
import datetime as dt

def main():
    """
        input:
            1 dataset containing data of all clients per month, generated by split_csv_month.py
        procedure:
            transform timestamp from date to (year, week, weekday) => this might enable the analysis of weekly trends
        output:
            1 dataset containing data of all clients per month with adapted date format
    """
    data_path = "../consumption_data/monthlyConsumption/"
    l_year = ["2011", "2012", "2013", "2014"]
    
    for year in l_year: 
    
        # extract data per month for each year
        for x in range(1,13):
            month =  "%02d" % x 
            input_file = year + "-" + month + "-" + "eletricity_consumption.csv"
            df = pd.read_csv((data_path + input_file), sep = ",", index_col = False)
            
            # transform date/time strings to datetime
            df["date"] = pd.to_datetime(df["date"], format ='%Y-%m-%d').dt.date
            df["time"] = pd.to_datetime(df["time"], format = '%H:%M:%S').dt.time
            
            new_df = pd.DataFrame()
            new_df["consumption"] = df["consumption"]
            new_df["pid"] = df["pid"]
            new_df["address"] = df["address"]
            
            new_df["year"] = df["date"].apply(lambda x: x.isocalendar().year)
            new_df["week"] = df["date"].apply(lambda x: x.isocalendar().week)
            new_df["weekday"] = df["date"].apply(lambda x: x.isocalendar().weekday)
            
            time_d = dict([(y,x) for x,y in enumerate(sorted(set(df["time"])))])
            new_df["time"] = pd.Series([time_d[x] for x in df["time"]])
            
            output_file = "transformed_date_" +  input_file
            new_df.to_csv((data_path + output_file), sep = ",", index = False)
        
    # 2015 has only data for 1.1. at midnight (0 o'clock)
    year = "2015"
    month = "01"
    input_file = year + "-" + month + "-" + "eletricity_consumption.csv"
    df = pd.read_csv((data_path + input_file), sep = ",", index_col = False)
    
    # transform date/time strings to datetime
    df["date"] = pd.to_datetime(df["date"], format ='%Y-%m-%d').dt.date
    df["time"] = pd.to_datetime(df["time"], format = '%H:%M:%S').dt.time
    
    new_df = pd.DataFrame()
    new_df["consumption"] = df["consumption"]
    new_df["pid"] = df["pid"]
    new_df["address"] = df["address"]
    
    new_df["year"] = df["date"].apply(lambda x: x.isocalendar().year)
    new_df["week"] = df["date"].apply(lambda x: x.isocalendar().week)
    new_df["weekday"] = df["date"].apply(lambda x: x.isocalendar().weekday)
    
    time_d = dict([(y,x) for x,y in enumerate(sorted(set(df["time"])))])
    new_df["time"] = pd.Series([time_d[x] for x in df["time"]])
    
    output_file = "transformed_date_" +  input_file
    new_df.to_csv((data_path + output_file), sep = ",", index = False)

if __name__ == "__main__":
    main()