from fastapi import FastAPI

# create an api object
app = FastAPI()

# ---EndPoint--


inventory = {
    1: {
        "name": "Milk",
        "price": 45,
        "Brand": "amrit"
    }
}


# @app.get("/get-item/{name}")
# def home(name: str):
#     for i in range(0, len(inventory)):
#         if inventory[i].items.has_key == name:
#             return inventory[i]


@app.get("/get-item/{id}")
def home(id: int):
    return inventory[id]
