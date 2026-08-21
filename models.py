from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)


class TextResponse(BaseModel):
    task: str
    result: str
    model_used: str
    tokens_used: int | None = None