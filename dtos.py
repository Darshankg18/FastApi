from pydantic import BaseModel

class productDTO(BaseModel):
    id:int
    title:str
    Price:int=0
    Count:int=0