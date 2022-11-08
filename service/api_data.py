from typing import Optional
import httpx
from models.Characters_Models import CharacterModel as model

#asincronico es cuando trabaja en paralelo, se pueden ejecutar distintas ejecuciones en distintos tiempos, para que multiples personas puedan llamar la api
async def get_characterById(characterID:int)->Optional(model):
    url = f"https://rickandmortyapi.com/api/character/{characterID}"
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
        response.raise_for_status()
        data=response.json()
        character= model(**data)#extraido desde data
        return character
    