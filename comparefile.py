import pandas as pd
data=pd.read_csv('C:\Users\hs\Desktop\m2018.csv')
data2=pd.read_csv('C:\Users\hs\Desktop\out2018.csv')
df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

for i1 in range(0,len(df['number'])):
    for j1 in range(0,len(df2['number'])):
        if df.at[i1,'Season'] is 'Spring':
            if df2.at[int(j1),'Season'] is 'Winter':
                if df.at[i1,'Day of week']  in  df2.at[int(j1),'Day of week']:
                   if df.at[i1,'Station']  in  df2.at[int(j1),'Station']:
                       df[i1,'Market Sharebeforeseason']=(df2.at[int(j1),'Market Share_total']/df2.at[int(j1),'Number'])
                       break
        if df.at[i1,'Season'] is 'Summer':
            if df2.at[int(j1),'Season'] is 'Spring':
                if df.at[i1,'Day of week']  in  df2.at[int(j1),'Day of week']:
                   if df.at[i1,'Station']  in  df2.at[int(j1),'Station']:
                       df[i1,'Market Sharebeforeseason']=(df2.at[int(j1),'Market Share_total']/df2.at[int(j1),'Number'])
                       break
        if df.at[i1,'Season'] is 'Fall':
            if df2.at[int(j1),'Season'] is 'Summer':
                if df.at[i1,'Day of week']  in  df2.at[int(j1),'Day of week']:
                   if df.at[i1,'Station']  in  df2.at[int(j1),'Station']:
                       df[i1,'Market Sharebeforeseason']=(df2.at[int(j1),'Market Share_total']/df2.at[int(j1),'Number'])
                       break
