from fastapi import FastAPI

from routes.credential_route import router as credential_router
from routes.workflow_route import router as workflow_router
app = FastAPI()

app.include_router(credential_router)

app.include_router(workflow_router)