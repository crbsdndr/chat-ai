from pydantic import BaseModel
from typing import Optional

class HTTPSuccessful(BaseModel):
    status_code: int
    detail: str
    header: Optional[dict] = None