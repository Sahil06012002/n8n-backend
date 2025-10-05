from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.credential_route import router as credential_router
from routes.workflow_route import router as workflow_router
app = FastAPI()

origins = [
    "http://localhost:5173",  # your frontend origin (Vite default)
    "http://localhost:3000",  # if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],     # GET, POST, DELETE, etc.
    allow_headers=["*"],
)

app.include_router(credential_router)

app.include_router(workflow_router)