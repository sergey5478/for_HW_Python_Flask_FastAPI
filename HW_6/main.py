import uvicorn
from fastapi import FastAPI
from HW_6.db import db
from HW_6.routes import users_1, goods_1, orders_1

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(users_1.router, tags=['users'])
app.include_router(goods_1.router, tags=['goods'])
app.include_router(orders_1.router, tags=['orders'])


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        # host="127.0.0.1",
        # port=8000,
        reload=True
    )
