import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def load_data(path):
    return pd.read_csv(path, encoding="latin1")

def preprocess_data(df):
    df['flight_day'] = df['flight_day'].map({"Mon":1, "Tue":2, "Wed":3, "Thu":4, "Fri":5, "Sat":6, "Sun":7})
    df['route'] = df.groupby('route')['booking_complete'].transform('mean')
    df['booking_origin'] = df.groupby('booking_origin')['booking_complete'].transform('mean')
    encoder = OneHotEncoder(sparse_output=False)
    one_hot = encoder.fit_transform(df[['sales_channel', 'trip_type']])
    one_hot_df = pd.DataFrame(one_hot, columns=encoder.get_feature_names_out(['sales_channel', 'trip_type']))
    df = df.drop(columns=['sales_channel', 'trip_type'])
    df = pd.concat([df.reset_index(drop=True), one_hot_df], axis=1)
    return df
