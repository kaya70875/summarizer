from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.response_models import *
from app.spacy.sumy_alg import summarize_paragraph

router = APIRouter()

# Define a request model for input validation
class SummarizeRequest(BaseModel):
    paragraph: str
    r: float = 0.3

@router.post("/summarize" , response_model= SummarizeResponseModel, description="Summarize an article")
async def summarize_text(request: SummarizeRequest):
    try:
        if not request.paragraph.strip():  # Ensure the text is not empty or just whitespace
            raise HTTPException(status_code=400, detail="Paragraph cannot be empty.")

        summary = summarize_paragraph(request.paragraph, request.r)
        return {"summary": summary}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
