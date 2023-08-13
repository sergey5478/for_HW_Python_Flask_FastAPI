import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()


class UserIn(BaseModel):
    """Наследник BaseModel."""
    name: str
    email: str
    password: str


class User(UserIn):
    """Наследник UserIn."""
    id: int


users = []


@app.get('/', response_model=list[User])
async def read_root():
    """Начало."""
    return users


@app.post('/user/', response_model=User)
async def create_user(item: UserIn):
    """POST."""
    id_user = len(users) + 1
    user = User
    user.id = id_user
    user.name = item.name
    user.email = item.email
    user.password = item.password
    users.append(user)
    return user


@app.get('/user/{id}', response_model=User)
async def get_task_by_id_root(id_user: int):
    """Get task."""
    for user in users:
        if user.id == id_user:
            return user


@app.put('/user/{id}', response_model=User)
async def put_task_by_id_root(id_user: int, new_user: UserIn):
    """PUT."""
    for user in users:
        if user.id == id_user:
            user.name = new_user.name
            user.email = new_user.email
            user.password = new_user.password
            return user
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/user/{id}")
async def delete_user(id_user: int):
    """DELETE."""
    for user in users:
        if user.id == id_user:
            users.remove(user)
            return users
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/message/")
async def read_message():
    """MESSAGE."""
    message = {"users": users}
    return JSONResponse(content=message, status_code=200)


if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
