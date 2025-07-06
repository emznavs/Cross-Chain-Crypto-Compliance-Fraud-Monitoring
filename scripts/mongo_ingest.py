from pymongo import MongoClient
from datetime import datetime
import certifi

docs = [
  {"user_id":"usr1","timestamp":datetime(2025,6,25,9,12,34),"event_type":"signup","wallet_type":"MetaMask","device_id":"devA","ip":"198.51.100.23","geo":{"country":"US","lat":37.77,"lon":-122.42}},
  {"user_id":"usr1","timestamp":datetime(2025,6,25,9,13,10),"event_type":"login","wallet_type":"MetaMask","device_id":"devA","ip":"198.51.100.23","geo":{"country":"US","lat":37.77,"lon":-122.42}},
  {"user_id":"usr1","timestamp":datetime(2025,6,25,9,14,0),"event_type":"transfer","wallet_type":"MetaMask","device_id":"devA","ip":"198.51.100.23","geo":{"country":"US","lat":37.77,"lon":-122.42}},
  {"user_id":"usr2","timestamp":datetime(2025,6,25,9,13,12),"event_type":"signup","wallet_type":"Coinbase","device_id":"devB","ip":"203.0.113.42","geo":{"country":"UK","lat":51.51,"lon":-0.13}},
  {"user_id":"usr2","timestamp":datetime(2025,6,25,9,15,20),"event_type":"quote_request","wallet_type":"Coinbase","device_id":"devB","ip":"203.0.113.42","geo":{"country":"UK","lat":51.51,"lon":-0.13}},
  {"user_id":"usr2","timestamp":datetime(2025,6,25,9,16,0),"event_type":"transfer","wallet_type":"Coinbase","device_id":"devB","ip":"203.0.113.42","geo":{"country":"UK","lat":51.51,"lon":-0.13}},
  # Bot-like repeated rapid transactions by usr3
  {"user_id":"usr3","timestamp":datetime(2025,6,25,9,17,0),"event_type":"transfer","wallet_type":"MetaMask","device_id":"devC","ip":"198.51.100.50","geo":{"country":"US","lat":40.71,"lon":-74.0}},
  {"user_id":"usr3","timestamp":datetime(2025,6,25,9,17,10),"event_type":"transfer","wallet_type":"MetaMask","device_id":"devC","ip":"198.51.100.50","geo":{"country":"US","lat":40.71,"lon":-74.0}},
  {"user_id":"usr3","timestamp":datetime(2025,6,25,9,17,20),"event_type":"transfer","wallet_type":"MetaMask","device_id":"devC","ip":"198.51.100.50","geo":{"country":"US","lat":40.71,"lon":-74.0}},
]

client = MongoClient("mongodb+srv://eanavidi:zjxpZggqMwtkCRrz@en-cluster.bklfh2l.mongodb.net/?retryWrites=true&w=majority&appName=EN-Cluster", tlsCAFile=certifi.where())
db = client.blockbridge
db.user_events.delete_many({})
db.user_events.insert_many(docs)
print("MongoDB Atlas seeded with improved data")
