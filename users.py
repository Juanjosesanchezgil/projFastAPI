from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad User

class User(BaseModel ):
    name : str
    surname : str
    url : str
    age : int

users_list = [User(name="Brais", surname="Moure", url="https://moure.dev", age=35),
         User(name="Moure", surname="Dev", url="https://mouredev.com", age=35),
         User(name="Juan", surname="Sanchez", url="https://juansanchez.dev", age=39),
         ]
    

@app.get("/usersjson")
async def usersjson():
    return [{"name" : "Brais", "surname" : "moure", "url" : "https://moure.dev", "age" : "35" },
            {"name" : "Moure", "surname" : "Dev", "url" : "https://mouredev.com", "age" : "35" },
            {"name" : "Juanj", "surname" : "Sanchez", "url" : "https://juansanchez.dev", "age" : "39" }]
    
@app.get("/users")
async def users():
    return users_list