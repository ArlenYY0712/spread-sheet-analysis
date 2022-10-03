# place your code to clean up the data file below.
import pandas as pd
import numpy as np
data = pd.read_csv("data/players_fifa23.csv")

data.index = np.arange(1, len(data) + 1)
data = data.rename(columns = {'ID' : 'Ranking'})
data['Ranking'] = data.index

#Only selecting the top 2000 rated players
data = data.sort_values(by = 'Overall', ascending = False)
data_new = data.head(2000)


#Dropping irrelevant columns such as PhotoURL, and specific ratings
data_new = data_new.drop(data_new.iloc[:,25:-1], axis = 1)
data_new = data_new.drop(data_new.columns[[6]], axis = 1)

df = data_new.iloc[: , :-1]

df.to_csv('data/clean_data.csv',index = False, encoding='utf-8')



