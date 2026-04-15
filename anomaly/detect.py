from pyod.models.iforest import IForest

def detect_anomalies(df):
    model = IForest()
    df['anomaly'] = model.fit_predict(df[['amount']])
    return df[df['anomaly'] == 1]
