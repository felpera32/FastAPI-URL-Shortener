from pydantic import BaseModel, HttpUrl

class linkValidator(BaseModel):
    link: HttpUrl