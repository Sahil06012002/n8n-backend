from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db_conn = os.getenv("DATABASE_CONNECTION")


_client = None

def get_database() :
    global _client
    if _client == None :    
        _client = AsyncMongoClient(db_conn)
    db = _client["n8n"]

    return db
