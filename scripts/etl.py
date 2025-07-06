import pandas as pd
from pymongo import MongoClient
from sqlalchemy import create_engine
import certifi

# MongoDB Atlas
client = MongoClient("mongodb+srv://eanavidi:zjxpZggqMwtkCRrz@en-cluster.bklfh2l.mongodb.net/?retryWrites=true&w=majority&appName=EN-Cluster", tlsCAFile=certifi.where())
events = pd.DataFrame(client.blockbridge.user_events.find())

# SQLite
engine = create_engine("sqlite:///data/blockbridge.db")
txns = pd.read_sql("SELECT * FROM onchain_txns", engine)

# Save raw
events.to_csv("data/raw/user_events.csv", index=False)
txns.to_csv("data/raw/onchain_txns.csv", index=False)
print("ETL complete")

