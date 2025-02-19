from pydantic import BaseModel

class SummarizeResponseModel(BaseModel):
    summary: list
    efficiency: float