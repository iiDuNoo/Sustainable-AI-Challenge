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


input_sample = pd.DataFrame({'Timestamp': pd.Series(['2003-05-01T00:00:00.000Z'], dtype='datetime64[ns]'), 'Holiday & Weekends': pd.Series(['False'], dtype='bool'), 'Price_Ott': pd.Series(['27.01'], dtype='float64'), 'OTT_Temperature': pd.Series(['8.9'], dtype='float64'), 'OTT_Dew Point': pd.Series(['5.1'], dtype='float64'), 'OTT_Relative Humidity': pd.Series(['77.0'], dtype='float64'), 'OTT_Wind Speed': pd.Series(['4.0'], dtype='float64')})


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = Model.get_model_path(model_name = 'AutoMLc96d2522832')
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
