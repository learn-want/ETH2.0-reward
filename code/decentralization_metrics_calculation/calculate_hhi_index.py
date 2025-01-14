import pandas as pd
import numpy as np
from tqdm import tqdm
from datetime import date



def calculate_hhi(df,column_name):
    """
    Compute HHI index of a DataFrame with a 'value' column, in our case, it is reward data
    df: DataFrame, the data to be used for HHI index calculation
    The return value is the HHI index with the float type
    """
    df['column_name'] = df[column_name].astype(float)
    df['prop'] = df['column_name']/df['column_name'].sum() 
    SQ = df['prop']**2
    V = SQ.sum()
    return V
    # return (V-1/len(df))/(1-1/len(df))


if __name__ == "__main__":
    start = date(2022,9,15)
    end = date(2023,9,16)
    #please change the path of date_validator_reward.csv to your local path
    reward=pd.read_parquet('data/raw_reward_data/daily_validator_index_reward/total_validator_reward.parquet')
    reward['date']=pd.to_datetime(reward['date']).dt.date
    # reward=reward[(reward['date']>pd.to_datetime('2022-09-15'))&(reward['date']<pd.to_datetime('2022-11-16'))]
    reward=reward.sort_values(by=['date'])
    reward.set_index('date',inplace=True)
    reward1=reward[['Total reward','Proposer reward','Attestation reward','Sync committee reward']]
    index_name='HHI'
    for j in tqdm(reward1.columns):
        reward1[j]=reward1[j].astype(float)
        #convert negative to 0
        if j in ['Total reward','Attestation reward']:
            reward1[j]=np.where(reward1[j]<0,0,reward1[j])
            reward1.reset_index(inplace=True)
            data=reward1
        # only keep positive numbers for proposer reward and sync committee reward, calculate HHI index between validators who get rewards
        else:
            data=reward1[reward1[j] > 0]
        file_name="_".join([i.lower() for i in j.split(' ')])
        with open(f'data/decentralization_metrics_data/{index_name}_{j}.csv', 'a') as file:
            reward_name=j.split(' ')[0] 
            file.write(f'date,{reward_name.lower()}\n')
            for day in tqdm(pd.date_range(start, end)):
                daily_data = data[(data['date'] == day.date())]
                if not daily_data.empty:
                    hhi_value =calculate_hhi(daily_data,j)  
                    file.write(f'{day.date()},{hhi_value}\n')

   