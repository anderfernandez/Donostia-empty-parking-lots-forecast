from skforecast.model_selection import grid_search_forecaster
from skforecast.ForecasterAutoregCustom import ForecasterAutoregCustom
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def create_predictors(y):
    '''
    Create the first 10 lags.
    Calculate the moving average of the last 20 values
    '''
    
    X_train = pd.DataFrame({'y':y.copy()})
    for i in range(0, 10):
        X_train[f'lag_{i+1}'] = X_train['y'].shift(i)
        
    X_train['moving_avg'] = X_train['y'].rolling(20).mean()
    
    X_train = X_train.drop(columns='y').tail(1).to_numpy()  
    
    return X_train  

def train_forecaster(train_data, test_data, param_grid, output_path,
                    method ='cv', metric = 'mean_squared_error'):

    # Grid search de hiperparámetros
    forecaster_rf = ForecasterAutoregCustom(
                        regressor      = RandomForestRegressor(random_state=123),
                        fun_predictors = create_predictors,
                        window_size    = 20
                    )
    
    # Hiperparámetros del regresor
    param_grid = {
    'n_estimators': [100, 500],
    'max_depth': [3, 5, 10]
    }

    resultados_grid = grid_search_forecaster(
                            forecaster  = forecaster_rf,
                            y           = train_data,
                            param_grid  = param_grid,
                            steps       = 10,
                            method      = method,
                            metric      = metric,
                            initial_train_size    = int(len(train_data)*0.5),
                            allow_incomplete_fold = True,
                            return_best = True,
                            verbose     = False
                        )
    
    return resultados_grid