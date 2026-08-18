from pydantic import BaseModel, Field
class Student(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0, lt=100)
    program: str = Field(min_length=2)