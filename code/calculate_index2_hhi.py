import pandas as pd
import numpy as np
from tqdm import tqdm
from datetime import date, timedelta, datetime
from decimal import Decimal
from tqdm import tqdm

def read_large_csv(file_path, chunk_size=1000000):
    accumulated_data = pd.DataFrame()
    chunks = pd.read_csv(file_path, chunksize=chunk_size)
    for chunk in chunks:
        accumulated_data = pd.concat([accumulated_data, chunk])
    return accumulated_data


def index(df):
    df['value'] = df['value'].astype(float)
    df['prop'] = df['value']/df['value'].sum() 
    H = -df['prop']*np.log2(df['prop'])
    E = H.sum()
    V = 2**E
    return V

# def HHI(df):
#     df['value'] = df['value'].astype(float)
#     df['prop'] = df['value']/df['value'].sum() 
#     SQ = df['prop']**2
#     V = SQ.sum()
#     return V
def HHI(df):
    df['value'] = df['value'].astype(float)
    df['prop'] = df['value']/df['value'].sum() 
    SQ = df['prop']**2
    V = SQ.sum()
    return V
    # return (V-1/len(df))/(1-1/len(df))

def gini(df):
    """
    Compute Gini coefficient of a DataFrame with a 'value' column
    """
    # Check if the DataFrame is empty or the 'value' column does not exist
    if df.empty or 'value' not in df.columns:
        return None 
    # Extract the 'value' column and convert it to a sorted list
    values = sorted(df['value'].tolist())
    # Check if the list is empty
    if len(values) == 0:
        return None
    # Compute the cumulative sum of the values
    cum_values = [0] + list(pd.Series(values).cumsum())
    n = len(values)
    # Calculate Gini coefficient using the formula
    numer = sum([(i+1) * values[i] for i in range(n)])
    denom = n * sum(values)
    if denom == 0:
        return None  # Avoid division by zero
    gini = (2 * numer) / denom - (n + 1) / n
    return gini

def nakamoto(df):
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

from datetime import date
start = date(2022,9,15)
end = date(2022,11,15)

def index_calc(data, start, end, index_type = index):
    duration= pd.date_range(start=start, end=end)
    days = np.size(duration)
    IndexValues = pd.DataFrame(np.zeros(days), columns=[f'{data.columns[1]}'])
    IndexValues['date'] = duration

    for i in tqdm(range(0, days)):
        start_date = start + timedelta(days=i)
        end_date = start_date + timedelta(days=1)
        IndexValues.loc[i,f'{data.columns[1]}'] = index_type(data[(data['date'].dt.date >= start_date) & (data['date'].dt.date < end_date)].copy())
    return IndexValues

if __name__ == "__main__":
    reward=read_large_csv('/local/scratch/exported/Ethereum_token_txs_data/rewards/total_rewards_daily_validator_each_validator_appear_once_daily.csv')
    reward['date']=reward['date'].astype('datetime64[ns]')
    # reward=reward[(reward['date']>pd.to_datetime('2022-09-15'))&(reward['date']<pd.to_datetime('2022-11-16'))]
    reward=reward.sort_values(by=['date'])
    # reward1=reward1.head(10000)
    reward1=reward[['date','Total reward','Proposer reward','Attestation reward','Sync committee reward']]
    reward1.set_index('date',inplace=True)
    # reward1=reward1/Decimal(10**9)
    # index_name=['nakamoto','index','gini','HHI'] #'nakamoto'
    index_name=['HHI']
    # indexs=[nakamoto,index,gini,HHI]
    indexs=[HHI]
    # index_name=[nakamoto]
    for i in tqdm(range(len(indexs))):  
        res=pd.DataFrame()  
        for j in tqdm(reward1.columns):
            reward1[j]=reward1[j].apply(float)
            if indexs[i] in [index,gini,HHI]:
                #把负数变成0
                if j in ['Total reward','Attestation reward']:
                    reward1[j]=np.where(reward1[j]<0,0,reward1[j])
                    data=reward1[j].reset_index()  
                else:
                    data=reward1[j][reward1[j] >= 0]
                    data=data.reset_index()  
                data['value']=data[j]
            else:
                if j in ['Total reward','Attestation reward']:
                    reward1[j]=np.where(reward1[j]<0,0,reward1[j])  #把负数变成0
                    data=reward1[j].reset_index()  
                else:
                    #只保留大于0的数
                    data=reward1[j][reward1[j] >=0]
                    data=data.reset_index()  
                data['value']=data[j]
            IndexValues=index_calc(data, start, end, index_type =indexs[i])
            IndexValues.to_csv(f'/home/user/yan/github/ETH2.0-reward/figure/index_data_4/{index_name[i]}_{j}_1124.csv')
            # res=pd.concat([res,IndexValues[f'{j}']],axis=1)
        # res.to_csv('./'+str(i)+'.csv')
        
   