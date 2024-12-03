import pandas as pd
from tqdm import tqdm
from datetime import timedelta
import numpy as np

def read_large_csv(file_path, chunk_size=1000000):
    """
    This function reads a large CSV file in chunks and returns the accumulated data
    file_path: str, the path to the CSV file
    chunk_size: int, the size of each chunk to be read
    the return value is a DataFrame with the accumulated data
    """
    accumulated_data = pd.DataFrame()
    chunks = pd.read_csv(file_path, chunksize=chunk_size)
    for chunk in chunks:
        accumulated_data = pd.concat([accumulated_data, chunk])
    return accumulated_data

def index_calc(data, start, end, index_type):
    """
    This function calculates the index values for a given time period
    data: DataFrame, the data to be used for index calculation
    start: datetime, the start date of the time period
    end: datetime, the end date of the time period
    index_type: function, the index calculation function, including shannon_entropy, HHI, gini,nakamoto
    the return value is a DataFrame with the index values for each day in the time period
    """
    duration= pd.date_range(start=start, end=end)
    days = np.size(duration)
    IndexValues = pd.DataFrame(np.zeros(days), columns=[f'{data.columns[1]}'])
    IndexValues['date'] = duration

    for i in tqdm(range(0, days)):
        start_date = start + timedelta(days=i)
        end_date = start_date + timedelta(days=1)
        IndexValues.loc[i,f'{data.columns[1]}'] = index_type(data[(data['date'].dt.date >= start_date) & (data['date'].dt.date < end_date)].copy())
    return IndexValues