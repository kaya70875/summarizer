import fastapi
from fastapi.middleware.cors import CORSMiddleware
from app.routes.summarize import router as summarize_router
import nltk

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Register routes
app.include_router(summarize_router, tags=["summarize"])

nltk.data.path.append('./nltk_data')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)