from tqdm import tqdm
from glob import glob
import pandas as pd
import os


##Generate the aggregated reward data combining the proposer, attestation and sync reward
proposer_reward=pd.read_parquet('data/raw_reward_data/proposer_reward_epoch_147262_147487.parquet')
proposer_reward['epoch']=proposer_reward['epoch'].astype('int64')
proposer_reward['epoch_v_index']=proposer_reward['epoch'].astype('str')+'_'+proposer_reward['proposer_index'].astype('int64').astype('str')
proposer_reward1=proposer_reward.groupby(by=['epoch_v_index','epoch'])[['total','attestations','sync_aggregate','proposer_slashings','attester_slashings']].sum()
proposer_reward1=proposer_reward1.reset_index()
proposer_reward1.rename(columns={'total':'proposer_total_reward','attestations':'proposer_attestations','sync_aggregate':'proposer_sync_aggregate','proposer_slashings':'proposer_proposer_slashings','attester_slashings':'proposer_attester_slashings'},inplace=True)

sync=pd.read_parquet('data/raw_reward_data/sync_reward_epoch_147262_147487.parquet')
sync['epoch']=sync['epoch'].astype('int64')
sync['epoch_v_index']=sync['epoch'].astype('str')+'_'+sync['validator_index'].astype('int64').astype('str')
sync1=sync.groupby(by=['epoch_v_index','epoch'])[['reward']].sum()
sync1=sync1.reset_index()
sync1.rename(columns={'reward':'sync_total_reward'},inplace=True)

file='data/raw_reward_data/attestation_reward_epoch_147262_147487.parquet'
start_epoch=file.split('/')[-1].split('.')[0].split('_')[-2]
end_epoch=file.split('/')[-1].split('.')[0].split('_')[-1]
validator_reward=pd.read_parquet(file)
validator_reward['attestation_total_reward']=validator_reward['head']+validator_reward['target']+validator_reward['source']
validator_reward['epoch_v_index']=validator_reward['epoch'].astype('int64').astype('str')+'_'+validator_reward['validator_index'].astype('int64').astype('str')
validator_reward_add_proposer=validator_reward.merge(proposer_reward1, on='epoch_v_index', how='left')
validator_reward_add_proposer_sync=validator_reward_add_proposer.merge(sync1, on='epoch_v_index', how='left')
# validator_reward_add_proposer_sync.to_parquet(f'data/raw_reward_data/aggregated_rewards/aggregated_rewards_{start_epoch}_{end_epoch}.parquet')

timestamp=pd.read_parquet('data/raw_reward_data/timestamp_epoch_147262_147487.parquet')
timestamp['time']=pd.to_datetime(timestamp['timestamp'],unit='s')
#Calculate the timestamp of the first slot of each epoch
epoch_timestamp=timestamp.groupby(by=['epoch'])[['time']].min().reset_index()
epoch_timestamp['time']=epoch_timestamp['time'].astype('str')
epoch_timestamp1 = pd.DataFrame(epoch_timestamp)
epoch_timestamp1['time']=epoch_timestamp1['time'].astype('datetime64[ns]')
validator_reward_add_proposer_sync['final_total_reward']=validator_reward_add_proposer_sync['attestation_total_reward']+validator_reward_add_proposer_sync['proposer_total_reward']+validator_reward_add_proposer_sync['sync_total_reward'] 
validator_reward_add_proposer_sync_time=validator_reward_add_proposer_sync.merge(epoch_timestamp1, on='epoch', how='left')
# validator_reward_add_proposer_sync_time=validator_reward_add_proposer_sync_time.drop(['epoch_epoch'])
validator_reward_add_proposer_sync_time['date']=validator_reward_add_proposer_sync_time['time'].dt.date
    
epoch_attestor_reward=validator_reward_add_proposer_sync_time.groupby(['epoch','validator_index'])[['final_total_reward','proposer_total_reward','attestation_total_reward','sync_total_reward']].sum().reset_index()
epoch_attestor_reward.to_csv(f'data/raw_reward_data/aggregated_rewards/epoch_validator_aggregated_data_{start_epoch}_{end_epoch}.csv',header=True,index=False)
epoch_attestor_reward.to_parquet(f'data/raw_reward_data/aggregated_rewards/epoch_validator_aggregated_data_{start_epoch}_{end_epoch}.parquet')

