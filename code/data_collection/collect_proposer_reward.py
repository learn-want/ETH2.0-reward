import json
import csv
from tqdm import tqdm
import numpy as np
import requests
from web3.beacon import Beacon
beacon = Beacon("http://localhost:1234") ##please change this to your beacon chain node url

def get_block_rewards(block_id):
    """
    Get rewards for a specific slot number on the beacon chain
    """
    url = f"http://localhost:1234/eth/v1/beacon/rewards/blocks/{block_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# An example of how to use the function
start_block = 0
end_block = 1000000
filename='your_file_path.csv' #please change this to your local path,do not put it in the data folder because it will be too large
with open(filename, 'a', newline='') as csvfile:
    for slot in tqdm(range(start_block, end_block)):
        rewards = get_block_rewards(slot)
        if rewards is not None:
            res = json.loads(rewards)
            block_reward=res['data']
            block_reward['slot']=slot
            fieldnames = block_reward.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if slot==start_block:
                # writer.writeheader() #追加时不重新写入header
                writer.writerow(block_reward)
            else:
                writer.writerow(block_reward)