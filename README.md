# Donostia empty parking lots forecast

## Objective
The final goal of this repo is to build an MLOps pipeline for a model that predicts the number of empty parking lots in Donostia. 
Right now the repo only includes the automation of the data extraction. 

## Automating the data extraction with Github Actions
The data is the core of this model. However, Donostia does not provide historical data of empty parking lots. Thus, the dataset must be created through periodical data extraction. 
The extraction of the data is done with the file `extract_data.py` in the `data_extraction` folder. 

This file just calls the endpoint where the data resides, it keeps important columns, add the timestamp and appends it to the file `data.csv` in the  `data` folder. 

Besides, within the `data_extraction` folder we can find the file `update_data.sh`, which is a bash script that pushes the newly generated file into Github. 

The execution of these two files is automated through `update_data.yml` Github Aciton workflow, which exectues the files every two hours.