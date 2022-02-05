import pandas as pd
import os
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.ensemble import RandomForestRegressor
from skforecast.model_selection import grid_search_forecaster
import pickle

# Data 
data_path = 'data/data.csv'
model_path = 'docker/model.pickle'
parking_prediction = 'Boulevard'
n_steps = 48


# Read the data
data = pd.read_csv(data_path)

# Filter the data for a single parking
data = data.loc[data['properties.nombre'] == parking_prediction, ['properties.libres', 'timestamp']]
data = data.reset_index(drop=True)


# Train test split 
data_train = data[:-n_steps]['properties.libres']
data_test  = data[-n_steps:]['properties.libres']

# Parameters grid search
forecaster = ForecasterAutoreg(
                regressor = RandomForestRegressor(random_state=123),
                lags      = 12
             )

# Hiperparámetros del regresor
param_grid = {
'n_estimators': [100, 500],
'max_depth': [3, 5, 10]
}

# Lags used as predictors
lags_grid = [24, 48, 72]

resultados_grid = grid_search_forecaster(
                        forecaster  = forecaster,
                        y           = data_train,
                        param_grid  = param_grid,
                        lags_grid   = lags_grid,
                        steps       = 10,
                        metric      = 'mean_squared_error',
                        initial_train_size    = int(len(data_train)*0.9),
                        return_best = True,
                        verbose = False
                    )

# We could now log data into metadata store like Neptune

# Save model and last training date as pickle
last_training_date = data[:-n_steps]['timestamp'].values[-1]
pickle.dump(last_training_date, open('docker/last_training_date.pickle', 'wb'))

pickle.dump(forecaster, open(model_path, 'wb'))