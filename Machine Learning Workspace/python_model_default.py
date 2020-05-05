
# The script MUST define a class named AzureMLModel.
# This class MUST at least define the following three methods: "__init__", "train" and "predict".
# The signatures (method and argument names) of all these methods MUST be exactly the same as the following example.


import pandas as pd
from sklearn.linear_model import Sequential


class AzureMLModel:
    # The __init__ method is only invoked in module "Create Python Model",
    # and will not be invoked again in the following modules "Train Model" and "Score Model".
    # The attributes defined in the __init__ method are preserved and usable in the train and predict method.
    def __init__(self):
        # self.model must be assigned
        self.model = Sequential()
        self.model.add(LSTM(50, activation='relu',input_shape=(n_steps,n_features)))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam',loss='mse')
        self.feature_column_names = list()

    # Train model
    #   Param<df_train>: a pandas.DataFrame
    #   Param<df_label>: a pandas.Series
    def train(self, df_train, df_label):
        # self.feature_column_names record the names of columns used for training
        # It is recommended to set this attribute before training so that later the predict method
        # can use the columns with the same names as the train method
        self.feature_column_names = df_train.columns.tolist()
        self.model.fit(df_train, df_label)

    # Predict results
    #   Param<df>: a pandas.DataFrame
    #   Must return a pandas.DataFrame
    def predict(self, df):
        # Predict using the same column names as the training
        return pd.DataFrame({'Scored Labels': self.model.predict(df[self.feature_column_names])})
