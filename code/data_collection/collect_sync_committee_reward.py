import json
import csv
from tqdm import tqdm
import numpy as np
import requests
from web3.beacon import Beacon
import pandas as pd

beacon = Beacon("http://localhost:1234") ##please change this to your beacon chain node url

def get_sync_committee_rewards(slot, committee_members=None):
    url = f"http://localhost:1234/eth/v1/beacon/rewards/sync_committee/{slot}"
    headers = {"Content-Type": "application/json"}

    if committee_members is not None:
        payload = json.dumps(committee_members)
    else:
        payload = json.dumps([])

    response = requests.post(url, headers=headers, data=payload)
    # print(response.status_code)
    # print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        # print(response.status_code)
        return None