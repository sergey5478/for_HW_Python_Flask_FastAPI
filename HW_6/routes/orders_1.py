from HW_6.db import db, orders_db
from HW_6.models import Orders, InputOrders
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


# Создание тестовых заказов
@router.get("/fake_orders/{count}")
async def create_note(count: int):
    for i in range(1, count + 1):
        query = orders_db.insert().values(
            user_id=f'user_id_{i}',
            goods_id=f'goods_{i}',
            order_date=f'order_date_{i}',
            status_order=f'status_order_{i}@mail.ru')
        await db.execute(query)
    return {'message': f'{count} fake orders create'}


# Создание нового заказа
@router.post("/orders/new/", response_model=Orders)
async def create_orders(orders: InputOrders):
    query = orders_db.insert().values(
        user_id=orders.user_id,
        goods_id=orders.goods_id,
        order_date=orders.order_date,
        status_order=orders.status_order)
    last_record_id = await db.execute(query)
    return {**orders.dict(), "id": last_record_id}


# Список заказов
@router.get("/orders/", response_model=list[Orders])
async def read_orders():
    query = orders_db.select()
    return await db.fetch_all(query)


# Просмотр одного заказа
@router.get("/orders/id/{orders_id}", response_model=Orders)
async def read_orders(orders_id: int):
    query = orders_db.select().where(orders_db.c.id == orders_id)
    return await db.fetch_one(query)


# Редактирование заказа
@router.put("/orders/replace/{orders_id}", response_model=Orders)
async def update_orders(orders_id: int, new_orders: InputOrders):
    query = orders_db.update() \
        .where(orders_db.c.id == orders_id) \
        .values(**new_orders.dict())
    await db.execute(query)
    return {**new_orders.dict(), "id": orders_id}


# Удаление заказа
@router.delete("/orders/del/{orders_id}")
async def delete_orders(orders_id: int):
    query = orders_db.delete().where(orders_db.c.id == orders_id)
    await db.execute(query)
    return {'message': 'Orders deleted'}
