from fastapi import FastAPI, HTTPException
from sheets import get_all, append_values_to_sheet
from github import get_user_info


app = FastAPI()


# GET request to retrieve all items
@app.get("/items")
async def read_items():
    return get_all()

# POST request to add a new item
@app.post("/items")
async def create_item(username: str):
    return append_values_to_sheet("Sheet2", get_user_info(username))
