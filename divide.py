# -*- coding: utf-8 -*-
#!/user/bin/env python3
import pandas as pd
import datetime
import sys

output_file = sys.argv[1]
#in_inter = sys.argv[2]
#in_toll = sys.argv[3]

#int_toll=int(in_toll)

#read "training.csv" with header=0, index column = vehicle_id and just read the columns writing in usecols attribute. 
df=pd.read_csv('trajectories(table 5)_training.csv',header=0,usecols=['intersection_id','tollgate_id','vehicle_id','starting_time','travel_time','travel_seq'],index_col=['vehicle_id'])
df['starting_time'] = pd.to_datetime(df.starting_time)  #turn df.starting_time's attribute to datetime


#setting starting time
st = '2016/7/19 08:00'

base = pd.to_datetime(st)   #make starting time into panda's datetime format which called base
#setting the timedelta variable.
numdays = 91    #setting the days you want to make in list.
numbmin = 7     #setting the range of minutes you wanna see. ex: 7 is from 08:00~10:00 seperating by 20 minutes.

#date_list contains all of datetimes to be compared by pulsing starting time by timedelta we set before.
#example: date_list[0]=2016/07/19 08:00
#         date_list[1]=2016/07/19 08:20
#         date_list[2]=2016/07/19 08:40
#         date_list[3]=2016/07/19 09:00
#         date_list[4]=2016/07/19 09:20....
date_list = [base + datetime.timedelta(days=x)+ datetime.timedelta(minutes=(20*y))
             for x in range(0, numdays) for y in range(0,numbmin)]
dl = pd.DataFrame(date_list)

run = 0     #loop counting

for i in range(1, (numdays*numbmin)):
    run += 1
    if i%numbmin==0:
        continue
    else:
        if run == 1:
            
            df.loc[(df.starting_time >= date_list[i-1]) #comparing if the df.starting_time is late to date_list[0](2016/07/19 08:00) 
                & (df.starting_time <= date_list[i]) #comparing if the df.starting_time is before to date_list[1](2016/07/19 08:20)
                 ].to_csv(output_file) #selecting the row whose tollgate_id is 3 and writing it into output.csv 
            
        else:
            df.loc[(df.starting_time >= date_list[i-1]) 
                & (df.starting_time <= date_list[i])
                ].to_csv(output_file, mode='a') #writring into output.csv,but just "adding" instead of overwriting.
            
#.to_csv('Mean.csv', mode='a',header=None,index=None)