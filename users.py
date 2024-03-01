from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad User

class User(BaseModel ):
    id : int
    name : str
    surname : str
    url : str
    age : int

users_list = [User(id= 1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
         User(id= 2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
         User(id= 3, name="Juan", surname="Sanchez", url="https://juansanchez.dev", age=39),
         ]
    

@app.get("/usersjson")
async def usersjson():
    return [{"name" : "Brais", "surname" : "moure", "url" : "https://moure.dev", "age" : "35" },
            {"name" : "Moure", "surname" : "Dev", "url" : "https://mouredev.com", "age" : "35" },
            {"name" : "Juanj", "surname" : "Sanchez", "url" : "https://juansanchez.dev", "age" : "39" }]
    
@app.get("/users")
async def users():
    return users_list

# Path

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    
# Query
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)
    

    
    
def search_user(id: int):
    
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error" : "No se ha encontrado el usuario"}