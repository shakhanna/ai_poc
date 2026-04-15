def explain_anomalies(anomalies):
    prompt = f"""
    Explain why these anomalies might occur:
    {anomalies.to_dict()}
    """
