from pydantic import BaseModel, Field


class InputUser(BaseModel):
    first_name: str = Field(title="first_name", min_length=2)
    last_name: str = Field(title="last_name", min_length=2)
    password: str = Field(title="password", min_length=3)
    email: str = Field(title="email", min_length=5)


class User(InputUser):
    id: int


class InputGoods(BaseModel):
    name: str = Field(title="name", min_length=2)
    description: str = Field(title="description", min_length=2)
    price: str = Field(title="price", min_length=3)


class Goods(InputGoods):
    id: int


class InputOrders(BaseModel):
    us_id: int
    goods_id: int
    date: str
    status: str


class Orders(BaseModel):
    id: int
    user: User
    goods: Goods
    date: str
    status: str
