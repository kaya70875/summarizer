from pydantic import BaseModel

class SummarizeResponseModel(BaseModel):
    summary: list