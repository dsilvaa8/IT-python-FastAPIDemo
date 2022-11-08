from pydantic import BaseModel

class CharacterModel(BaseModel):
    name: str
    status: str
    species: str
    gender: str