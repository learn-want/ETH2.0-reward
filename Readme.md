# Ethereum 2.0 PoS Beacon Chain Rewards Analysis Repository README

Welcome to the repository for the analysis of beacon chain rewards within the Ethereum 2.0 Proof of Stake (PoS) framework. This repository is designed as a resource for academic researchers, blockchain developers, and anyone interested in studying the reward mechanisms of the Ethereum blockchain in detail. Specifically, the replication code for: "Analyzing Reward Dynamics and Decentralization in Ethereum 2.0: An Advanced Data Engineering Workflow and Comprehensive Datasets for Proof-of-Stake Incentives."

## Contents
- [Introduction](#ethereum-20-pos-beacon-chain-rewards-analysis-repository-readme)
  - [Contents](#contents)
  - [Structure of the Repository](#structure-of-the-repository)
    - [Python Code](#python-code)
    - [Sample Data](#sample-data)
    - [Visualizations](#visualizations)
    - [Data Collection Scripts](#data-collection-scripts)
  - [Initial Setup](#initial-setup)

## Structure of the Repository

### Python Code
Located here is the Python code for data manipulation and analysis, principally utilizing Jupyter Notebooks.

### Sample Data
Sample datasets are provided in this directory in the form of compact CSV files. These samples represent a variety of beacon chain rewards and metrics.
The `date_validator_reward.csv` file is not contained within this directory due to its size but can be retrieved from the Harvard Dataverse at:

> Yan, Tao; Li, Shengnan; Kraner, Benjamin; Zhang, Luyao; Tessone, Claudio J., 2024, "Replication Data for: 'Analyzing Reward Dynamics and Decentralization in Ethereum 2.0: An Advanced Data Engineering Workflow and Comprehensive Datasets for Proof-of-Stake Incentives'", Harvard Dataverse, V1.

### Visualizations
This section includes the data visualizations generated from the processed data, which range from simple charts to complex graphical plots.

### Data Collection Scripts
Scripts used to gather data directly from the Ethereum blockchain are stored here. Please replace the placeholder with your specific beacon chain node URL.

## Initial Setup
To get started with this repository:
1. Clone the repository to your local machine.
2. Install Python and the necessary dependencies listed in `requirements.txt`.
3. Acquire a beacon chain node URL to facilitate data collection.
4. Execute the scripts within the `script` directory to gather initial datasets.
5. Navigate to the `data` directory to review the datasets. For the full dataset, download the `date_validator_reward.csv` file from the provided Harvard Dataverse link and place it in the `data` directory.
6. Utilize the Jupyter Notebooks in the `code` directory for data processing and analysis.
7. Generate or examine existing visualizations in the `figures` directory.
