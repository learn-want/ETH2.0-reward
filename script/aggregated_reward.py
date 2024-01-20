from tqdm import tqdm
from glob import glob
import vaex
import pandas as pd


##Generate the aggregated reward data combining the proposer, attestation and sync reward
proposer_reward=vaex.from_csv('../data/rewards/slot_proposer_reward.csv')
proposer_reward['epoch']=proposer_reward['epoch'].astype('int64')
proposer_reward['epoch_v_index']=proposer_reward['epoch'].astype('str')+'_'+proposer_reward['proposer_index'].astype('int64').astype('str')
proposer_reward1=proposer_reward.groupby(by=['epoch_v_index','epoch'], agg={'total': 'sum','attestations':'sum','sync_aggregate':'sum',
                                                 'proposer_slashings':'sum','attester_slashings':'sum'})

sync=vaex.from_csv('../data/rewards/sync_committee_reward.csv')
sync['epoch']=sync['epoch'].astype('int64')
sync['epoch_v_index']=sync['epoch'].astype('str')+'_'+sync['validator_index'].astype('int64').astype('str')
sync1=sync.groupby(by=['epoch_v_index','epoch'],agg={'reward':'sum'})

files=glob('../data/rewards/attestation_reward_*.csv')
for file in tqdm(files):
    start_epoch=file.split('/')[-1].split('.')[0].split('_')[-2]
    end_epoch=file.split('/')[-1].split('.')[0].split('_')[-1]
   
   
    validator_reward=vaex.from_csv(file)
    validator_reward['total_reward']=validator_reward['head']+validator_reward['target']+validator_reward['source']
    validator_reward['epoch_v_index']=validator_reward['epoch'].astype('int64').astype('str')+'_'+validator_reward['validator_index'].astype('int64').astype('str')
    validator_reward_add_proposer=validator_reward.join(proposer_reward1, on='epoch_v_index', how='left', rsuffix='_proposer')
    validator_reward_add_proposer_sync=validator_reward_add_proposer.join(sync1, on='epoch_v_index', how='left', rsuffix='_sync')
    validator_reward_add_proposer_sync=validator_reward_add_proposer_sync.drop(['epoch_proposer','epoch_sync'])
    validator_reward_add_proposer_sync.export_hdf5(f'../data/rewards/aggregated_rewards/aggregated_rewards_{start_epoch}_{end_epoch}.hdf5')



timestamp=pd.read_csv('../data/slot_timestamp.csv')
timestamp['time']=pd.to_datetime(timestamp['timestamp'],unit='s')
#Calculate the timestamp of the first slot of each epoch
epoch_timestamp=timestamp.groupby(by=['epoch'])[['time']].min().reset_index()
epoch_timestamp['time']=epoch_timestamp['time'].astype('str')
epoch_timestamp1 = vaex.from_pandas(epoch_timestamp)
epoch_timestamp1['time']=epoch_timestamp1['time'].astype('datetime64[ns]')

files=glob('../data/aggregated_rewards/aggregated_rewards*.hdf5')
for file in tqdm(files):
    df=vaex.open(file)
    df.rename('total',new_name='proposer_total_reward')
    df.rename('total_reward',new_name='attestation_total_reward')
    df.rename('attestations',new_name='proposer_attestations')
    df.rename('sync_aggregate',new_name='proposer_sync_aggregate')
    df.rename('attester_slashings',new_name='proposer_attester_slashings')
    df.rename('reward',new_name='sync_total_reward')
    df['proposer_total_reward'] = df.func.where(df.epoch_v_index_proposer.isna()==True, 0,df.proposer_total_reward)
    df['proposer_attestations'] = df.func.where(df.epoch_v_index_proposer.isna()==True, 0,df.proposer_attestations)
    df['proposer_sync_aggregate'] = df.func.where(df.epoch_v_index_proposer.isna()==True, 0,df.proposer_sync_aggregate)
    df['proposer_slashings'] = df.func.where(df.epoch_v_index_proposer.isna()==True, 0,df.proposer_slashings)
    df['proposer_attester_slashings'] = df.func.where(df.epoch_v_index_proposer.isna()==True, 0,df.proposer_attester_slashings)
    df['sync_total_reward'] = df.func.where(df.epoch_v_index_sync.isna()==True, 0,df.sync_total_reward)
    df['final_total_reward']=df['attestation_total_reward']+df['proposer_total_reward']+df['sync_total_reward'] 
    df_time=df.join(epoch_timestamp1, on='epoch', how='left', rsuffix='_epoch')
    df_time=df_time.drop(['epoch_epoch'])
    df_time['date']=df_time['time'].dt.date
    
    epoch_attestor_reward=df_time.groupby(by=['epoch'],agg={'final_total_reward':'sum','proposer_total_reward':'sum','attestation_total_reward':'sum','sync_total_reward':'sum'}).to_pandas_df() 
    epoch_attestor_reward.to_csv(f'../data/epoch_validator_aggregated_data.csv',mode='a',header=False,index=False)
 