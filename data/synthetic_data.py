from faker import Faker
import pandas as pd

fake = Faker()

def generate_data(n=1000):
    return pd.DataFrame([{
        "customer_id": fake.random_int(),
        "amount": fake.random_number(digits=3),
        "timestamp": fake.date_time()
    } for _ in range(n)])
