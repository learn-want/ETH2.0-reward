# README for Ethereum 2.0 PoS Beacon Chain Rewards Analysis Repository

This repository hosts the sample datasets and Python codebase for the analysis of beacon chain rewards in the Ethereum 2.0 Proof of Stake (PoS) framework. It is designed to facilitate comprehensive investigations into the dynamics of consensus rewards on the Ethereum blockchain, tailored for academics, blockchain developers, and other stakeholders.

As the validator reward data set has a large size, and it is time-consuming to collect data from the Beacon chain node, we only provide a sample of the data set in this repository. The full data set of beacon chain rewards in the first two months after the Merge is available at Harvard Dataverse: url.

## Table of Contents
- [README for Ethereum 2.0 PoS Beacon Chain Rewards Analysis Repository](#readme-for-ethereum-20-pos-beacon-chain-rewards-analysis-repository)
  - [Table of Contents](#table-of-contents)
  - [Repository Structure](#repository-structure)
    - [Code](#code)
    - [Data](#data)
    - [Figures](#figures)
    - [Script](#script)
  - [Getting Started](#getting-started)

## Repository Structure

### Code
This folder contains the Python code for data processing, primarily developed in Python and encapsulated within Jupyter Notebook environments.

### Data
Here, you'll find the sample data in small CSV files, encompassing various aspects of beacon chain rewards and related metrics.
`date_validator_reward.csv` is not in this folder because of its large size. You can download it from Harvard Dataverse:

Yan, Tao; Li, Shengnan; Kraner, Benjamin; Zhang, Luyao; Tessone, Claudio J., 2024, "Replication Data for: "Analyzing Reward Dynamics and Decentralization in Ethereum 2.0: An Advanced Data Engineering Workflow and Comprehensive Datasets for Proof-of-Stake Incentives"", https://doi.org/10.7910/DVN/OKQRS1, Harvard Dataverse. 

### Figures
Contains visualizations of the processed data, including graphs, charts, and other graphical representations.

### Script
This folder holds the scripts for data collection from Ethereum's blockchain and other sources.

please change this to your beacon chain url.

## Getting Started
1. Clone the repository.
2. Install Python and required libraries (`requirements.txt`).
3. Get a beacon chain node URL.
4. Run data collection scripts in the `script` folder to collect some sample    data.
5. Explore the `data` folder for datasets. Download the full dataset named `date_validator_reward.csv` and put into in the data folder.
6. Process and analyze data using the Jupyter Notebooks in the `code` folder.
7. View or create visualizations in the `figures` folder.
