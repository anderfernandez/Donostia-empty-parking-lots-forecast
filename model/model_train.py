import pandas as pd
from statsmodels.tsa.stattools import adfuller
from train_utils import train_forecaster

# Data 
data_path = 'data/data.csv'
ouput_path = 'data/predictions.csv'

# Read the data
data = pd.read_csv(data_path)

# Group data by parking
for name, group in data.groupby('properties.nombre'):
    
    output_path = f'{output_path}/group'