from bson import ObjectId
from fastapi import HTTPException
from database.main import get_database
from models.credentials import Credentials


db = get_database()
credential_conn = db["credentials"]


async def insert_credential(credentials : Credentials) :
    result = await credential_conn.insert_one(credentials)

    return result


async def fetch_credential_by_id(id) :
    try : 
        oid = ObjectId(id)
        credential = await credential_conn.find_one({"_id" : oid})
        return credential
    
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid credential Id")
    

async def fetch_user_credentials(user_id : str) :
    credentials = []
    async for credential in credential_conn.find({"user_id" : user_id}) :
        credentials.append(credential)
    return credentials


async def delete_credential_by_id(credential_id) :
    try :
        oid = ObjectId(credential_id)
        result = await credential_conn.delete_one({"_id": oid})
        return result
    except :
        raise HTTPException(status_code=400 , detail="Invalid credential Id")
