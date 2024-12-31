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