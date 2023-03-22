from peewee import *
from datetime import datetime

db = SqliteDatabase(
    "webshop.db",
    pragmas={"journal_mode": "wal", "foreign_keys": 1, "ignore_check_constraints": 0},
)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = AutoField()
    username = CharField(max_length=20, null=False, unique=True)
    street = CharField(max_length=40)
    house_number = CharField(max_length=10)  # e.g. "139 E" is also possible !
    postal_code = CharField(max_length=6)
    city = CharField(max_length=30)
    country = CharField(max_length=30)
    billing_info = CharField(max_length=100)


class Product(BaseModel):
    product_id = AutoField()
    name = CharField(max_length=20, null=False, index=True)
    description = CharField(max_length=50, null=False, index=True)
    price = DecimalField(
        decimal_places=2,
        auto_round=True,
        default=0,
        constraints=[Check("price < 1000000")],
    )
    quantity = IntegerField(default=0, constraints=[Check("quantity < 1000")])
    owner = ForeignKeyField(User, backref="products")


class Tag(BaseModel):
    tag_id = AutoField()
    name = CharField(max_length=20, null=False, unique=True)


class ProductTag(BaseModel):
    producttag_id = AutoField()
    product = ForeignKeyField(Product, backref="producttags")
    tag = ForeignKeyField(Tag, backref="producttags")


class Transaction(BaseModel):
    transaction_id = AutoField()
    buyer = ForeignKeyField(User, backref="transactions")
    product_bought = ForeignKeyField(Product, backref="products")
    quantity_bought = IntegerField(
        default=0, constraints=[Check("quantity_bought < 1000")]
    )
    date_time = DateTimeField(default=datetime.now())
