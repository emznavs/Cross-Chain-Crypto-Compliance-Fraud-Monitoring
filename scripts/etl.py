import pandas as pd
from pymongo import MongoClient
from sqlalchemy import create_engine
import certifi

# MongoDB Atlas connection & fetch user events
client = MongoClient("mongodb+srv://eanavidi:zjxpZggqMwtkCRrz@en-cluster.bklfh2l.mongodb.net/?retryWrites=true&w=majority&appName=EN-Cluster", tlsCAFile=certifi.where())
events = pd.DataFrame(client.blockbridge.user_events.find())

# SQLite connection & fetch onchain transactions
engine = create_engine("sqlite:///data/blockbridge.db")
txns = pd.read_sql("SELECT * FROM onchain_txns", engine)

# Save raw data for next steps
events.to_csv("data/raw/user_events.csv", index=False)
txns.to_csv("data/raw/onchain_txns.csv", index=False)

print("ETL complete - raw CSV files saved.")
