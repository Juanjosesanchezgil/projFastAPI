from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def users():
    return [{"name" : "Brais", "surname" : "moure", "url" : "https://moure.dev" },
            {"name" : "Moure", "surname" : "Dev", "url" : "https://mouredev.com" },
            {"name" : "Juanj", "surname" : "Sanchez", "url" : "https://juansanchez.dev" }]