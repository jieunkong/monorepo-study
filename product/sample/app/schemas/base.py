from pydantic import BaseModel


class BaseRequest(BaseModel):
    """
    request data format
    """
    name: str


class BaseReponse(BaseModel):
    """
    response data format
    """
    # id: int
    name: str
    