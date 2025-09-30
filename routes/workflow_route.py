from fastapi import APIRouter

from database.worflow_repository import insert_workflow , fetch_user_workflows , fetch_workflow_by_id
from models.workflow import WorkFlow


router = APIRouter(
    prefix="/workflow",
    tags=["workflow"]
)


# currently mongo data is directly passed as str 
# TODO : change the mongo data according to the requirement and then send that in json format


@router.post("")
async def add_workflow(workflow : WorkFlow) :

    result = insert_workflow(workflow)

    return {
        "reslut" : str(result)
    }

@router.get("/user/{user_id}")
async def get_workflows(user_id : str) :

    result = await fetch_user_workflows(user_id)

    return {
        "credentials" : str(result)
    }

@router.get("/{workflow_id}")
async def get_workflow_by_id(workflow_id) :
    workflow = await fetch_workflow_by_id(workflow_id)

    return {
        "workflow" : str(workflow)
    }

@router.get("/webhook/handler/{id}")
async def excute_workflow(workflow_id : str) :
    workflow = "excution logic"

    return {
        "workflow" : str(workflow)
    }  
