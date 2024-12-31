
import json
import requests
from web3.beacon import Beacon
import warnings
warnings.filterwarnings("ignore")

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