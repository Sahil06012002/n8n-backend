from fastapi import APIRouter, Body

from database.credential_repository import delete_credential_by_id, insert_credential, fetch_credential_by_id , fetch_user_credentials
from models.credentials import Credentials


router = APIRouter(
    prefix="/credentials",
    tags=["credentials"]
)


@router.post("")
async def post_credentials(data :Credentials) :
    print(data)
    result = await insert_credential(data.model_dump())
    return {"result" : str(result.inserted_id) }


@router.get("/{credential_id}") 
async def get_credential(credential_id) :
    result = await fetch_credential_by_id(credential_id)

    return {
        "credential" : str(result)
    }

@router.get("/user/{user_id}") 
async def get_user_credentials(user_id : str) :
    result = await fetch_user_credentials(user_id)
    for cred in result:
        cred["_id"] = str(cred["_id"])
    return {
        "user-credentials" : str(result)
    }

@router.delete("/{credential_id}") 
async def delete_credential(credential_id) :
    result = await delete_credential_by_id(credential_id)
    return {
        "result" : str(result)
    }
