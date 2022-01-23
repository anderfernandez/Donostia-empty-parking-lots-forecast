# Load libraries
import pandas as pd
import requests
import os

# Define variables
url = 'https://www.donostia.eus/info/ciudadano/camaras_trafico.nsf/getParkings.xsp'
output_path = 'data'
current_path = '//data_extraction'
important_columns = ['properties.nombre', 'properties.libres']
output_filename = 'data.csv'

# Get the data
resp = requests.get(url)

# Convert resp to pandas DF
data = pd.json_normalize(
    resp.json()['features']
    )

# Select important columns
data = data.loc[:, important_columns]

# Add timestamp  column
data['timestamp'] = pd.Timestamp.now()

# Change dir to main
os.chdir(os.getcwd().replace(current_path, '')) 

# Check if file already exists
if output_filename in os.listdir(output_path):

    # Read existing data
    existing_data = pd.read_csv(f'{output_path}/{output_filename}')

    # Concat both datasets
    final_data = pd.concat([existing_data,data])

else: 
    final_data = data.copy()

# Save the final dataset
final_data.to_csv(f'{output_path}/{output_filename}', index = False)
