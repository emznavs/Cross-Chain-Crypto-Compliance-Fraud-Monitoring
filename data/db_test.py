import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///blockbridge.db")

df = pd.read_sql("SELECT * FROM onchain_txns WHERE fee > 1.0", engine)
print(df)