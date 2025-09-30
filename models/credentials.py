from pydantic import BaseModel


class Credentials(BaseModel) :
    user_id  : str
    title : str
    platform : str
    data : dict