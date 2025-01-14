import json
import requests
from web3.beacon import Beacon

beacon = Beacon("http://localhost:1234") ##please change this to your beacon chain node url

def get_sync_committee_rewards(slot, committee_members=None):
    url = f"http://localhost:1234/eth/v1/beacon/rewards/sync_committee/{slot}"
    headers = {"Content-Type": "application/json"}

    if committee_members is not None:
        payload = json.dumps(committee_members)
    else:
        payload = json.dumps([])

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# An example of how to use the function
start_slot = 0
end_slot = 1000000
filename='your_file_path_sync_committee_reward.csv' #please change this to your local path,do not put it in the data folder because it will be too large
with open(filename, 'a', newline='') as csvfile:
    for slot in tqdm(range(start_slot, end_slot)):
        rewards = get_sync_committee_rewards(slot)
        if rewards is not None:
            res = json.loads(rewards)
            block_reward=res['data']
            block_reward['slot']=slot
            fieldnames = block_reward.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if slot==start_slot:
                writer.writerow(block_reward)
            else:
                writer.writerow(block_reward)