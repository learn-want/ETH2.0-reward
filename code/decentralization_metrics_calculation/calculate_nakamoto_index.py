import numpy as np
from tqdm import tqdm
from datetime import date
from tqdm import tqdm
import pandas as pd

def calculate_nakamoto(df,column_name):
    """
    Compute Nakamoto index of a DataFrame with a 'value' column, in our case, it is reward data
    df: DataFrame, the data to be used for Nakamoto index calculation
    The return value is the Nakamoto index with the int type
    """
    df[column_name] = df[column_name].astype(float)
    df.sort_values(by=[column_name],ascending=False,inplace=True)
    df.reset_index(inplace=True,drop=True)
    df.set_index(keys=df.index.values+1,inplace=True)
    df['prop'] = df[column_name]/df[column_name].sum() 
    df['cumprop'] = df['prop'].cumsum(axis=0)
    try:
        V = df[df['cumprop'] > 0.5].index[0]
        # return V/validator_number_one_day
        return V
    except:
        return 0


if __name__ == "__main__":
    start = date(2022,9,15)
    end = date(2024,1,1)    
   #please change the path of date_validator_reward.csv to your local path
    reward=pd.read_parquet('data/raw_reward_data/aggregated_rewards/total_validator_reward.parquet')
    reward['date']=pd.to_datetime(reward['date']).dt.date
    reward=reward.sort_values(by=['date'])
    reward.set_index('date',inplace=True)
    reward1=reward[['Total reward','Proposer reward','Attestation reward','Sync committee reward']]
    index_name='nakamoto'
    for j in tqdm(reward1.columns):
        reward1[j]=reward1[j].astype(float)
        if j in ['Total reward','Attestation reward']:
            reward1[j]=np.where(reward1[j]<0,0,reward1[j])  #convert negative to 0
            reward1.reset_index(inplace=True)
            data=reward1
        else:
            #only keep positive numbers
            data=reward1[j][reward1[j] > 0]
            data.reset_index(inplace=True)
        file_name="_".join([i.lower() for i in j.split(' ')])
        with open(f'data/decentralization_metrics_data/{index_name}_{j}.csv', 'a') as file:
            reward_name=j.split(' ')[0]
            file.write(f'date,{reward_name.lower()}\n')
            for day in tqdm(pd.date_range(start, end)):
                daily_data = data[(data['date'] == day.date())]
                if not daily_data.empty:
                    nakamoto_value =calculate_nakamoto(daily_data,j)
                    file.write(f'{day.date()},{nakamoto_value}\n')
            
   