import pandas as pd
import numpy as np
from tqdm import tqdm
from datetime import date
from tqdm import tqdm
from utility import read_large_csv
from utility import index_calc



def HHI(df):
    """
    Compute HHI index of a DataFrame with a 'value' column, in our case, it is reward data
    df: DataFrame, the data to be used for HHI index calculation
    The return value is the HHI index with the float type
    """
    df['value'] = df['value'].astype(float)
    df['prop'] = df['value']/df['value'].sum() 
    SQ = df['prop']**2
    V = SQ.sum()
    return V
    # return (V-1/len(df))/(1-1/len(df))


if __name__ == "__main__":
    start = date(2022,9,15)
    end = date(2022,11,15)
    #please change the path of date_validator_reward.csv to your local path
    reward=read_large_csv('/local/scratch/exported/Ethereum_token_txs_data/rewards/date_validator_reward.csv')
    reward['date']=reward['date'].astype('datetime64[ns]')
    # reward=reward[(reward['date']>pd.to_datetime('2022-09-15'))&(reward['date']<pd.to_datetime('2022-11-16'))]
    reward=reward.sort_values(by=['date'])
    reward1=reward[['date','Total reward','Proposer reward','Attestation reward','Sync committee reward']]
    reward1.set_index('date',inplace=True)
    index_name='HHI'
    for j in tqdm(reward1.columns):
        reward1[j]=reward1[j].apply(float)
        #convert negative to 0
        if j in ['Total reward','Attestation reward']:
            reward1[j]=np.where(reward1[j]<0,0,reward1[j])
            data=reward1[j].reset_index()  
        else:
            data=reward1[j][reward1[j] >= 0]
            data=data.reset_index()  
        data['value']=data[j]
        IndexValues=index_calc(data, start, end, index_type =HHI)
        IndexValues.to_csv(f'../figure/decentralization_metrics_data/{index_name}_{j}_1124.csv')
           
   