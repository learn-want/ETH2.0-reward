
import json
import requests
from web3.beacon import Beacon
import warnings
warnings.filterwarnings("ignore")
from utility import calculate_epoch_from_slot

beacon = Beacon("http://localhost:1234") ##please change this to your beacon chain node url

def get_attestations_rewards(epoch, validators=None):
    """
    Get rewards for attestations in a specific epoch
    epoch: int, the epoch number for which the attestation rewards are to be retrieved
    validators: list, the list of validator indices for which the rewards are to be retrieved, default is None
    """
    url = f"http://localhost:1234/eth/v1/beacon/rewards/attestations/{epoch}"
    headers = {"Content-Type": "application/json"}
    if validators is not None:
        payload = json.dumps(validators)
    else:
        payload = json.dumps([])

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None
head_slot=eval(beacon.get_syncing()['data']['head_slot'])
head_epoch=calculate_epoch_from_slot(head_slot)
eth2_start_epoch=0
for i in tqdm(range(eth2_start_epoch,head_epoch)):
    res=get_attestations_rewards(i)
    if res is None:
        pass
    else:
        attestation_total_rewards=res['data']['total_rewards']
        attestation_total_rewards=pd.DataFrame(attestation_total_rewards)
        attestation_total_rewards['epoch']=i
        
        if (i-eth2_start_epoch)%500==0: # save every 500 epochs due to the large size of the data
            filename = f'your_file_path_attestation_reward__{i}_{i+500}.csv'
            attestation_total_rewards.to_csv(filename,index=False)
        else:
            attestation_total_rewards.to_csv(filename,index=False,header=False,mode='a')
    
    