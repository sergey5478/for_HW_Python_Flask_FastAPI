from HW_6.db import db, goods_db
from HW_6.models import Goods, InputGoods
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


# Создание тестовых товаров
@router.get("/fake_goods/{count}")
async def create_note(count: int):
    for i in range(1, count + 1):
        query = goods_db.insert().values(
            name=f'name_{i}',
            description=f'description_{i}',
            price=f'price_{i}')
        await db.execute(query)
    return {'message': f'{count} fake users create'}


# Создание нового товара
@router.post("/goods/new/", response_model=Goods)
async def create_product(product: InputGoods):
    query = goods_db.insert().values(
        name=product.name,
        description=product.description,
        price=product.price)
    last_record_id = await db.execute(query)
    return {**product.dict(), "id": last_record_id}


# Список товаров
@router.get("/goods/", response_model=list[Goods])
async def read_goods():
    query = goods_db.select()
    return await db.fetch_all(query)


# Просмотр одного товара
@router.get("/goods/id/{product_id}", response_model=Goods)
async def read_product(product_id: int):
    query = goods_db.select().where(goods_db.c.id == product_id)
    return await db.fetch_one(query)


# Редактирование товара
@router.put("/goods/replace/{product_id}", response_model=Goods)
async def update_product(product_id: int, new_product: InputGoods):
    query = goods_db.update() \
        .where(goods_db.c.id == product_id) \
        .values(**new_product.dict())
    await db.execute(query)
    return {**new_product.dict(), "id": product_id}


# Удаление товара
@router.delete("/goods/del/{product_id}")
async def delete_product(product_id: int):
    query = goods_db.delete().where(goods_db.c.id == product_id)
    await db.execute(query)
    return {'message': 'product deleted'}
