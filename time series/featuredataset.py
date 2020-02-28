import sys
import pandas as pd
data=pd.read_csv('C:\Users\hs\Desktop\m2018.csv')


data['yearDate']=pd.to_datetime(data['Start_time'],format='%m/%d/%Y %H:%M').dt.year
data['month']=pd.to_datetime(data['Start_time'],format='%m/%d/%Y %H:%M').dt.month 
data['day']=pd.to_datetime(data['Start_time'],format='%m/%d/%Y %H:%M').dt.day
data['Stime'] =(pd.to_datetime(data['Start_time'],format='%m/%d/%Y %H:%M').dt.hour*60)+  pd.to_datetime(data['Start_time'],format='%m/%d/%Y %H:%M').dt.minute
data['Etime'] =(pd.to_datetime(data['End_time'],format='%m/%d/%Y %H:%M').dt.hour*60)+  pd.to_datetime(data['End_time'],format='%m/%d/%Y %H:%M').dt.minute 




data['Episode']=data['Episode'].str.encode(encoding = 'punycode')
data['Name of show']=data['Name of show'].str.encode(encoding = 'punycode')
data['Name of episode']=data['Name of episode'].str.encode(encoding = 'punycode')
data['Genre']=data['Genre'].str.encode(encoding = 'punycode')


df = pd.DataFrame(data)


df2 = pd.DataFrame([[0,2016,'Winter','Monday','V Total',0,0]],
                   index=[0], columns=['number','Year', 'Season','Day of week','Station','Market Share_total','Number'])

numberofdf2=0;
flag=0;
for i1 in range(0,len(df['number'])):
    for j1 in range(0,len(df2['number'])):
        if df.at[i1,'Season']  in  df2.at[int(j1),'Season']:
            if df.at[i1,'Day of week']  in  df2.at[int(j1),'Day of week']:
                if df.at[i1,'Station']  in  df2.at[int(j1),'Station']:
                    df2.at[int(j1),'Market Share_total']=(df2.at[int(j1),'Market Share_total']+df.at[i1,'Market Share_total'])
                    df2.at[int(j1),'Number']=(1+df2.at[int(j1),'Number'])
                    flag=1

    if flag==0:
        numberofdf2=(numberofdf2+1)
        df2.at[numberofdf2,'number']=int(numberofdf2)
        df2.at[numberofdf2,'Year']=2018
        df2.at[numberofdf2,'Season']=df.at[i1,'Season']
        df2.at[numberofdf2,'Day of week']=df.at[i1,'Day of week']
        df2.at[numberofdf2,'Station']=df.at[i1,'Station']
        df2.at[numberofdf2,'Market Share_total']=df.at[i1,'Market Share_total']
        df2.at[numberofdf2,'Number']=1
    flag=0
        
df2.to_csv('C:\Users\hs\Desktop\out2018.csv', index=False,line_terminator='')      
