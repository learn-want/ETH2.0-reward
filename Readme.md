# <span style="font-family: Arial, sans-serif; font-size: 2em; color: #4CAF50;">Ethereum 2.0 PoS Beacon Chain Rewards Analysis Repository</span>

<p style="font-family: Arial, sans-serif; font-size: 1.2em; line-height: 1.6;">
Welcome to the repository for analyzing beacon chain rewards within the <strong>Ethereum 2.0 Proof of Stake (PoS)</strong> framework. This repository is intended for academic researchers, blockchain developers, and enthusiasts interested in studying the reward mechanisms and decentralization of the Ethereum blockchain.
</p>

<p style="font-family: Arial, sans-serif; font-size: 1.2em; line-height: 1.6;">
This repository provides replication code and datasets for the working paper:
</p>

<blockquote style="background-color: #f9f9f9; border-left: 5px solid #4CAF50; padding: 10px; font-family: Georgia, serif; font-size: 1.1em; line-height: 1.6;">
<strong>"Analyzing Reward Dynamics and Decentralization in Ethereum 2.0: An Advanced Data Engineering Workflow and Comprehensive Datasets for Proof-of-Stake Incentives"</strong>
</blockquote>

<p style="font-family: Arial, sans-serif; font-size: 1.2em; line-height: 1.6;">
The full paper is available on <a href="https://arxiv.org/abs/2312.02660" style="color: #4CAF50; text-decoration: none;"><strong>arXiv:2312.02660</strong></a>.
</p>


---

## Table of Contents
- [Introduction](#ethereum-20-pos-beacon-chain-rewards-analysis-repository)
- [Structure of the Repository](#structure-of-the-repository)
  - [Data](#data)
  - [Python Code](#python-code)
  - [Visualizations](#visualizations)
- [Initial Setup](#initial-setup)
- [Reference](#reference)

---

## Structure of the Repository

### Data
This repository includes key datasets for analyzing Ethereum 2.0 beacon chain rewards and decentralization metrics.

#### Aggregated Reward Data on a Daily Basis
We provide one year (September 15, 2022 – September 15, 2023) of daily aggregated reward data for each validator. The dataset `total_validator_reward.parquet` includes various reward types. Due to its large size (3.3GB), the file is hosted on the Harvard Dataverse:

> [Yan, Tao; Li, Shengnan; Kraner, Benjamin; Zhang, Luyao; Tessone,Claudio J. 2025, "Replication Data for: Analyzing Reward Dynamics and Decentralization in Ethereum 2.0", Harvard Dataverse](https://doi.org/10.7910/DVN/HG36LO)

To use this data:
> Download the file and place it in the [`aggregated_rewards`](data/raw_reward_data/aggregated_rewards) directory.

##### Dataset Overview
| **Variable**               | **Data Type** | **Unit** |
|----------------------------|---------------|----------|
| date                       | date          | count    |
| validator_index            | int64         | count    |
| total_reward               | int64         | Ether    |
| attestation_reward         | int64         | Ether    |
| sync_committee_reward      | int64         | Ether    |
| proposer_reward            | int64         | Ether    |

#### Aggregated Reward Data on an Epoch Basis
Due to its size (1.5TB), only one day's epoch data (September 17, 2022) is provided. The dataset `epoch_validator_aggregated_data_147262_147487.parquet` is stored in the [`aggregated_rewards`](data/raw_reward_data/aggregated_rewards) directory.

- **Source Files**:
  - `proposer_reward_epoch_147262_147487.parquet`
  - `sync_reward_epoch_147262_147487.parquet`
  - `attestation_reward_epoch_147262_147487.parquet` (downloadable from the Harvard Dataverse; place it in the [`raw_reward_data`](data/raw_reward_data) directory).

#### Decentralization Metrics Data
This directory contains decentralization metrics such as:
- Gini coefficient
- HHI (Herfindahl-Hirschman Index)
- Shannon entropy
- Nakamoto coefficient

The data is in CSV format, with daily metrics.



### Python Code
The repository includes Python scripts for data collection, decentralization metrics calculation, and visualization:

- **Data Collection**:
  - Scripts are located in [`code/data_collection`](code/data_collection).
  - Replace placeholders in the scripts with your beacon chain node URL.

- **Decentralization Metrics Calculation**:
  - Scripts are located in [`code/decentralization_metrics_calculation`](code/decentralization_metrics_calculation).
  - These scripts compute metrics based on the collected data.

---

### Visualizations
Visualizations generated from the processed data include simple charts and complex plots. You can:

- View existing visualizations in the [`figure`](figure) directory.
- Generate plots using `result_plots.ipynb` to replicate figures from the working paper.

---

## Initial Setup
To set up the repository for data analysis:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/learn-want/ETH2.0-reward.git
   cd ETH2.0-reward
   ```

2. **Install Dependencies**:
   - Ensure Python is installed.
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Beacon Chain Node**:
   - Acquire a beacon chain node URL or run a local node.
   - Refer to [Teku Documentation](https://docs.teku.consensys.io/development/get-started/start-teku) for setting up a local Teku client in archive mode.

4. **Data Collection**:
   - Navigate to the code directory:
     ```bash
     cd code
     ```
   - Run data collection scripts in the [`data_collection`](code/data_collection) directory:
     ```bash
     python get_attestation_reward.py
     python get_proposer_reward.py
     python get_sync_committee_reward.py
     python aggregated_epoch_reward.py
     python aggregated_daily_reward.py
     ```
   - To collect example data, use:
     ```bash
     jupyter notebook collect_reward_beacon.ipynb
     ```

5. **Download Full Dataset**:
   - Download `total_validator_reward.parquet` from the [Harvard Dataverse](https://doi.org/10.7910/DVN/HG36LO) and place it in [`aggregated_rewards`](data/raw_reward_data/aggregated_rewards).

6. **Data Analysis**:
   - Use scripts in [`decentralization_metrics_calculation`](code/decentralization_metrics_calculation) for analysis.
   - Run `result_plots.ipynb` for visualizations.

7. **Data Validation**:
   - Validate collected data using `data_cross_validation.ipynb` in the [`code`](code) directory.

---

## Reference
For further details on this analysis, please refer to our working paper:  
**"Analyzing Reward Dynamics and Decentralization in Ethereum 2.0"**  
Available on [arXiv:2312.02660](https://arxiv.org/abs/2312.02660).
