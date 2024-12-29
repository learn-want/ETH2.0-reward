import pandas as pd
import numpy as np
from tqdm import tqdm
from datetime import date

def calculate_gini_index(df, column_name):
    """
    计算DataFrame中指定列的Gini系数
    df: DataFrame，包含要计算Gini系数的列
    column_name: str，列名
    返回值: float，Gini系数
    """
    # 检查DataFrame是否为空或指定列是否存在
    if df.empty or column_name not in df.columns:
        return None
    # 提取指定列并转换为排序后的列表
    values = sorted(df[column_name].tolist())
    # 检查列表是否为空
    if len(values) == 0:
        return None
    # 计算累积和
    cum_values = [0] + list(pd.Series(values).cumsum())
    n = len(values)
    # 使用公式计算Gini系数
    numer = sum([(i+1) * values[i] for i in range(n)])
    denom = n * sum(values)
    if denom == 0:
        return None  # 避免除以零
    gini = (2 * numer) / denom - (n + 1) / n
    return gini

if __name__ == "__main__":
    start = date(2022,9,15)
    end = date(2024,1,1)
    # please change the file path to your local path
    reward=pd.read_parquet('data/raw_reward_data/daily_validator_index_reward/total_validator_reward.parquet')
    reward['date']=pd.to_datetime(reward['date']).dt.date
    reward=reward.sort_values(by=['date'])
    reward.set_index('date',inplace=True)
    reward1=reward[['Total reward','Proposer reward','Attestation reward','Sync committee reward']]
    index_name='gini'
    for j in tqdm(reward1.columns):
        reward1[j]=reward1[j].astype(float)
        # change the negative value to 0
        if j in ['Total reward','Attestation reward']:
            reward1[j]=np.where(reward1[j]<0,0,reward1[j])
            reward1.reset_index(inplace=True)
            data=reward1
        else:
            data=reward1[j][reward1[j] > 0]
            data.reset_index(inplace=True)
        file_name="_".join([i.lower() for i in j.split(' ')])
        with open(f'data/decentralization_metrics_data/{index_name}_{j}.csv', 'a') as file:
            file.write(f'date,{j}\n')
            for day in tqdm(pd.date_range(start, end)):
                daily_data = data[(data['date'] == day.date())]
                if not daily_data.empty:
                    gini_value = calculate_gini_index(daily_data, j)
                    file.write(f'{day.date()},{gini_value}\n')

        
   