df = generate_data()

anomalies = detect_anomalies(df)

tests = generate_tests(schema)

explanation = explain_anomalies(anomalies)

docs = generate_docs(schema)
