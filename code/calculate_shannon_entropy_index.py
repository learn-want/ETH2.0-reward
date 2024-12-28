import pandas as pd
import numpy as np
from tqdm import tqdm
from datetime import date


def shannon_entropy(df,column_name):    
    """
    Compute Shannon entropy of a DataFrame with a 'value' column, in our case, it is reward data
    df: DataFrame, the data to be used for Shannon entropy calculation
    The return value is the Shannon entropy with the float type
    """
    df[column_name] = df[column_name].astype(float)
    df['prop'] = df[column_name]/df[column_name].sum() 
    H = -df['prop']*np.log2(df['prop'])
    E = H.sum()
    V = 2**E
    return V

if __name__ == "__main__":
    start = date(2022,9,15)
    end = date(2024,1,1)
    #please change the path of date_validator_reward.csv to your local path
    reward=pd.read_parquet('/local/scratch/exported/Ethereum_token_txs_data_TY_23/rewards/eth2_reward_ether/daily_validator_index_reward/total_validator_reward.parquet')
    reward['date']=pd.to_datetime(reward['date']).dt.date
    # reward=reward[(reward['date']>pd.to_datetime('2022-09-15'))&(reward['date']<pd.to_datetime('2022-11-16'))]
    reward=reward.sort_values(by=['date'])
    reward.set_index('date',inplace=True)
    reward1=reward[['Total reward','Proposer reward','Attestation reward','Sync committee reward']]
    index_name='Shannon'
    for j in tqdm(reward1.columns):
        reward1[j]=reward1[j].astype(float)
        reward1.reset_index(inplace=True)
        data=reward1
        #convert negative values to 0
        if j in ['Total reward','Attestation reward']:
            reward1[j]=np.where(reward1[j]<0,0,reward1[j])
            reward1.reset_index(inplace=True)
            data=reward1
        else:
            data=reward1[j][reward1[j] > 0]
            data.reset_index(inplace=True)
        file_name="_".join([i.lower() for i in j.split(' ')])
        with open(f'/home/user/yan/github/ETH2.0-reward/data/decentralization_metrics_data/{index_name}_{j}_new.csv', 'a') as file:
            reward_name=j.split(' ')[0] 
            file.write(f'date,{reward_name.lower()}\n')
            for day in tqdm(pd.date_range(start, end)):
                daily_data = data[(data['date'] == day.date())]
                if not daily_data.empty:
                    shannon_value =shannon_entropy(daily_data,j)
                    file.write(f'{day.date()},{shannon_value}\n')
   