# Ethereum 2.0 PoS Beacon Chain Rewards Analysis Repository README

Welcome to the repository for the analysis of beacon chain rewards within the Ethereum 2.0 Proof of Stake (PoS) framework. This repository is designed as a resource for academic researchers, blockchain developers, and anyone interested in studying the reward mechanisms of the Ethereum blockchain in detail. Specifically, the replication code for: "Analyzing Reward Dynamics and Decentralization in Ethereum 2.0: An Advanced Data Engineering Workflow and Comprehensive Datasets for Proof-of-Stake Incentives."

## Contents
- [Introduction](#ethereum-20-pos-beacon-chain-rewards-analysis-repository-readme)
  - [Contents](#contents)
  - [Structure of the Repository](#structure-of-the-repository)
    - [Data](#data)
    - [Python Code](#data-collection-and-analysis-scripts)
    - [Visualizations](#visualizations)
  - [Initial Setup](#initial-setup)

## Structure of the Repository

### Data

#### Aggregated reward data on a daily basis
We offer one-year (from September 15, 2022, to September 15, 2023) aggregated reward data that specifies the various types of daily rewards for each validator, named `total_validator_reward.parquet`. Due to its large size, this data is not included in this repository but can be accessed from the Harvard Dataverse at:

> [Yan, Tao; Li, Shengnan; Kraner, Benjamin; Zhang, Luyao; Tessone, 2025, "Replication Data for: Analyzing Reward Dynamics and Decentralization in1 Ethereum 2.0: A Data Engineering Workflow and2 Datasets", Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FHG36LO&showIngestSuccess=true&version=DRAFT). please firstly download the file and put it in the [aggregated_rewards](data/raw_reward_data/aggregated_rewards) directory.
we use the Parquet format to store data to reduce the storage space, still this file `total_validator_reward.parquet` has 3.3GB, the variable description is as follows:

| **Variable**               | **Data Type** | **Unit** |
|----------------------------|--------------|----------|
| date                     | date        | count    |
| validator_index           | int64        | count    |
| total reward     | int64        | Ether    |
| attestation reward        | int64        | Ether    |
| sync committee reward     | int64        | Ether    |
| proposer reward           | int64        | Ether    |
#### Aggregated reward data on an epoch basis
Due to the large size of the whole reward data on an epoch basis, which is more than 1.5 TB, We only provide aggregated reward data for a single day on an epoch basis, specifically on `2022-09-17`. this data is named "epoch_validator_aggregated_data_147262_147487.parquet" and is located in [aggregated_rewards](data/raw_reward_data/aggregated_rewards) directory.
This data is generated from   `proposer_reward_epoch_147262_147487.parquet`, `sync_reward_epoch_147262_147487.parquet` and `attestation_reward_epoch_147262_147487.parquet` files. The first two files are in the [aggregated_rewards](data/raw_reward_data/aggregated_rewards) directory. However, the attestation reward file is also stored on the Harvard Dataverse due to its large size. Please first download the file and put it in the [raw_reward_data](data/raw_reward_data) directory.

#### decentralization_metrics_data
This directory contains the decentralization metrics data, which includes the Gini coefficient, HHI,Shannon entropy, Nakamoto coefficient for each day. The data is stored in the csv format, and each file includes the date and the corresponding decentralization metrics.

### Python Code
Located here is the Python code for data collection and analysis.
The scripts in the sub-folder [data_collection](code/data_collection) are used to gather data directly from the Ethereum Beacon chain. Please replace the placeholder in the code with your specific beacon chain node URL. For the steps to execute the scripts, please refer to the [Initial Setup](#initial-setup) section.

The scripts in the sub-folder [decentralization_metrics_calculation](code/decentralization_metrics_calculation) are used to calculate the decentralization metrics. 


### Visualizations
This section includes the data visualizations generated from the processed data, which range from simple charts to complex graphical plots. You can find the visualizations in the [figure](figure) directory.

## Initial Setup
To get started with this repository:
1. Clone the repository to your local machine.
2. Get an Beacon Chain Node URL or run a local node.
please refer to [Teku](https://docs.teku.consensys.io/development/get-started/start-teku) to run the Teku cilent in the archive mode.
3. cd into the repository directory by executing `cd ETH2.0-reward`.
4. Install Python and the necessary dependencies by executing conda env  `pip install -r requirements.txt`.
5. Acquire a beacon chain node URL and put it into the data collection scripts in the [data_collection](code/data_collection).
6. Switch to the code folder by executing `cd code`, and execute the scripts within the [data_collection](code/data_collection) directory to gather full datasets,please follow the steps below:
    - run `get_attestation_reward.py`
    - run `get_proposer_reward.py`
    - run `get_sync_committee_reward.py`
    - run `aggregated_epoch_reward.py` to generate the aggregated reward data on an epoch basis.
    - run `aggregated_daily_reward.py` to generate the aggregated reward data on a daily basis.
    - If you just want to try to collect some example data, it is recommended to run `collect_reward_beacon.ipynb`.
7. Navigate to the [data](data) directory to review the datasets. For the full dataset, please download the `total_validator_reward.parquet` file from the provided Harvard Dataverse link and place it in the [aggregated_rewards](data/raw_reward_data/aggregated_rewards) directory.
8. Switch to the root directory by executing `cd ETH2.0-reward` and utilize the code in the [decentralization_metrics_calculation](code/decentralization_metrics_calculation/) directory for data processing and analysis.
9. Run the `result_plots.ipynb` to  generate plots of the paper or examine visualizations in the [figure](figure) directory.
10. To verify the data we collected, you can run the `data_cross_validation.ipynb` in the [code](code) directory.