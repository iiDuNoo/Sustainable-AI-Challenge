# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import pickle
import numpy as np
import pandas as pd
import azureml.train.automl
from sklearn.externals import joblib
from azureml.core.model import Model

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType


input_sample = pd.DataFrame({'Timestamp': pd.Series(['2003-05-01T00:00:00.000Z'], dtype='datetime64[ns]'), 'Holiday & Weekends': pd.Series(['0'], dtype='int64'), 'Price_Tor': pd.Series(['26.19'], dtype='float64'), 'TOR_Temperature': pd.Series(['7.2'], dtype='float64'), 'TOR_Dew Point': pd.Series(['4.8'], dtype='float64'), 'TOR_Relative Humidity': pd.Series(['85.0'], dtype='float64'), 'TOR_Wind Speed': pd.Series(['9.0'], dtype='float64')})


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = Model.get_model_path(model_name = 'AutoMLf340975e061')
    model = joblib.load(model_path)


@input_schema('data', PandasParameterType(input_sample, enforce_shape=False))
def run(data):
    try:
        y_query = None
        if 'y_query' in data.columns:
            y_query = data.pop('y_query').values
        result = model.forecast(data, y_query)
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})

    forecast_as_list = result[0].tolist()
    index_as_df = result[1].index.to_frame().reset_index(drop=True)
    
    return json.dumps({"forecast": forecast_as_list,   # return the minimum over the wire: 
                       "index": json.loads(index_as_df.to_json(orient='records'))  # no forecast and its featurized values
                      })
