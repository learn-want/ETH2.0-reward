import pandas as pd

def slot_to_timestamp(slot):
    """
    This function converts a slot number to a timestamp
    """
    return slot*12+1606824023

def slot_to_epoch(slot):
    """
    This function converts a slot number to an epoch number
    """
    return slot//32

def epoch_to_timestamp(epoch):
    """
    This function converts an epoch number to a timestamp
    """
    return epoch*384+1606824023

def timestamp_to_epoch(timestamp):
    """
    This function converts a timestamp to an epoch number
    """
    return (timestamp-1606824023)//384

def date_to_timestamp(date_str, latest=False):

    """

    Convert a date string to a timestamp.

    If latest is True, return the timestamp for the end of the day.

    """

    if latest:

        dt = pd.to_datetime(date_str) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

    else:

        dt = pd.to_datetime(date_str)

    return dt.timestamp()
