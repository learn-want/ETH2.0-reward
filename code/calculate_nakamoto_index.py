import numpy as np
from tqdm import tqdm
from datetime import date
from tqdm import tqdm
from utility import read_large_csv
from utility import index_calc

def nakamoto(df):
    """
    Compute Nakamoto index of a DataFrame with a 'value' column, in our case, it is reward data
    df: DataFrame, the data to be used for Nakamoto index calculation
    The return value is the Nakamoto index with the int type
    """
    # validator_number=pd.read_csv('/home/user/yan/github/ETH2.0-reward/daily_validator_number_new.csv')
    # validator_number_one_day=validator_number.loc[validator_number['date']==str((df['date'].dt.date.values[0])),'validator_index'].values[0]
    df['value'] = df['value'].astype(float)
    df.sort_values(by=['value'],ascending=False,inplace=True)
    df.reset_index(inplace=True,drop=True)
    df.set_index(keys=df.index.values+1,inplace=True)
    df['prop'] = df['value']/df['value'].sum() 
    df['cumprop'] = df['prop'].cumsum(axis=0)
    try:
        V = df[df['cumprop'] > 0.5].index[0]
        # return V/validator_number_one_day
        return V
    except:
        return 0


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
    index_name='nakamoto'
    for j in tqdm(reward1.columns):
        reward1[j]=reward1[j].apply(float)
        if j in ['Total reward','Attestation reward']:
            reward1[j]=np.where(reward1[j]<0,0,reward1[j])  #convert negative to 0
            data=reward1[j].reset_index()  
        else:
            #only keep positive numbers
            data=reward1[j][reward1[j] >= 0]
            data=data.reset_index()  
        data['value']=data[j]
        IndexValues=index_calc(data, start, end, index_type =nakamoto)
        IndexValues.to_csv(f'../figure/decentralization_metrics_data/{index_name}_{j}_1124.csv')
        
        
   