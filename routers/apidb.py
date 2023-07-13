from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://admin1:bbpadmin2022@atlascluster.aufwdcz.mongodb.net/?retryWrites=true&w=majority")
db = client["data"]
collection =db["data"]
router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"message": "Not found"}}
)

class Api(BaseModel):
    name: str
    title: str
    imgurl: str
    id: int


@router.get("/")
async def get_api():
    api = collection.find_one()
    if api:
        return {
            "_id" : str(api["_id"]),
            "id" : api["id"],
            "name" : api["name"],
            "title" : api["title"],
            "imgurl" : api["imgurl"]
        }
    else:
        raise HTTPException(status_code=404)

@router.get("/{api_id}")
async def get_api(api_id: int):
    api = collection.find_one({"id": api_id})
    if api:
        return {
            "_id" : str(api["_id"]),
            "id" : api["id"],
            "name" : api["name"],
            "title" : api["title"],
            "imgurl" : api["imgurl"]
        }
    else:
        raise HTTPException(status_code=404)

@router.post("")
async def create_api(api: Api):
    result = collection.insert_one(api.dict())
    return {
        "_id" : str(result.inserted_id),
        "id" : api.id,
        "name" : api.name,
        "title" : api.title,
        "imgurl" : api.imgurl
    }
@router.put("/{api_id}")
async def edit_api(api: Api):
    result = collection.update_one(api.dict())
    return {
        "_id" : str(result.inserted_id),
        "id" : api.id,
        "name" : api.name,
        "title" : api.title,
        "imgurl" : api.imgurl
    }
# @router.put("/{book_id}")
# async def edit_book(book_id: int, book: Book):
#     result = book.dict()
#     book_db[book_id].update(result)
#     return result

@router.delete("/{api_id}")
async def delete_api(api_id: int):
    result = collection.delete_one({"id": api_id})
    if result:
        return HTTPException(status_code=200)
    else:
        raise HTTPException(status_code=404)