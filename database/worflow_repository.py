from bson import ObjectId
from fastapi import HTTPException
from database.main import get_database
from models.workflow import WorkFlow


db = get_database()
db_conn = db["workflows"]


async def insert_workflow(workflow : WorkFlow) :
    
    result = await db_conn.insert_one(workflow)

    return result

async def fetch_user_workflows(user_id : str) :
    workflows = []

    async for workflow in db_conn.find({"user_id" : user_id}) :
        workflows.append(workflow)
    return workflows

async def fetch_workflow_by_id(workflow_id) :
    try :
        oid = ObjectId(workflow_id)
        workflow = await db_conn.find_one({"_id" : oid})
        return workflow
    except :
        raise HTTPException(status_code=400, detail="Invalid credential Id")
