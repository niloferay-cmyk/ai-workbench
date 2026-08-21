from typing import Optional
from pydantic import BaseModel, Field

class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=10000)  # FIXED: added max_length

class TextResponse(BaseModel):
    task: str
    result: str
    model: str
    tokens_used: Optional[int] = None  # FIXED: Optional[int] works on Python <3.10 too

class HealthResponse(BaseModel):
    status: str
    provider: str
    model: str