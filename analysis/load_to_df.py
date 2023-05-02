#!/user/bin/env python3
from dataformats import *
import numpy as np
import pandas as pd


# Class to import a Larus data logfile into a pandas dataframe.
class LoadLarus2Df:
    df = None

    def __init__(self, file):
        if file.endswith('.f123'):
            dataformat = data_f123
        elif file.endswith('.f110'):
            dataformat = data_f110
        else:
            print('Format, not supported')
            exit()

        # Create a pandas dataframe
        dt = np.dtype(dataformat)
        data = np.fromfile(file, dtype=dt, sep="")
        self.df = pd.DataFrame(data)

    def df(self):
        return self.df

