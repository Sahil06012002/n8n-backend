from pydantic import BaseModel


class WorkFlow(BaseModel) :
    user_id : str
    title : str
    enabled : bool
    nodes: dict
    connections : dict