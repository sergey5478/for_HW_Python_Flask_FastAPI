import databases
import sqlalchemy
from settings import settings

db = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()
users_db = sqlalchemy.Table("users", metadata,
                            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("first_name", sqlalchemy.String(32)),
                            sqlalchemy.Column("last_name", sqlalchemy.String(32)),
                            sqlalchemy.Column("password", sqlalchemy.String(64)),
                            sqlalchemy.Column("email", sqlalchemy.String(128)),
                            )

goods_db = sqlalchemy.Table("goods", metadata,
                            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("name", sqlalchemy.String(32)),
                            sqlalchemy.Column("description", sqlalchemy.String(128)),
                            sqlalchemy.Column("price", sqlalchemy.String(64)),
                            )

orders_db = sqlalchemy.Table("orders", metadata,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'),
                                               nullable=False),
                             sqlalchemy.Column("goods_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('goods.id'),
                                               nullable=False),
                             sqlalchemy.Column("order_date", sqlalchemy.String(128)),
                             sqlalchemy.Column("status_order", sqlalchemy.String(128)),
                             )

engine = sqlalchemy.create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False})
metadata.create_all(engine)
