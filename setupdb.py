from models import *
import os


def populate_test_data():
    path = os.path.join(os.getcwd(), "webshop.db")
    if os.path.exists(path):
        os.remove(path)

    db.connect()
    db.create_tables([User, Product, Tag, ProductTag, Transaction])

    piet = User.create(
        username="Piet",
        street="Lijnbaansgracht",
        house_number="139 E",
        postal_code="1016VV",
        city="Amsterdam",
        country="Holland",
        billing_info="Billing info Piet",
    )
    bob = User.create(
        username="Bob",
        street="Rozengracht",
        house_number="51",
        postal_code="1013NB",
        city="Amsterdam",
        country="Holland",
        billing_info="Billing info Bob",
    )
    kees = User.create(
        username="Kees",
        street="Koopelstokstraat",
        house_number="34",
        postal_code="1066RT",
        city="Amsterdam",
        country="Holland",
        billing_info="Billing info Kees",
    )

    tag_audio = Tag.create(name="audio")
    tag_video = Tag.create(name="video")
    tag_apple = Tag.create(name="apple")
    tag_samsung = Tag.create(name="samsung")
    tag_phone = Tag.create(name="phone")
    tag_tablet = Tag.create(name="tablet")
    tag_desktop = Tag.create(name="desktop")

    computer = Product.create(
        name="Computer",
        description="Een 2e hands PC uit 2015",
        price=150,
        quantity=3,
        owner=piet,
    )
    dvd_player = Product.create(
        name="DVD player",
        description="Een nieuwe DVD speler",
        price=75,
        quantity=2,
        owner=piet,
    )
    cd_player = Product.create(
        name="CD player", description="Deze zijn nieuw", price=65, quantity=4, owner=bob
    )
    ipad = Product.create(
        name="Ipad",
        description="Een nieuwe Ipad - model 2022",
        price=350,
        quantity=6,
        owner=bob,
    )
    iphone = Product.create(
        name="Iphone",
        description="Een refurbished Iphone",
        price=200,
        quantity=4,
        owner=kees,
    )
    samsung = Product.create(
        name="Samsung Galaxy",
        description="Een nieuwe Samsung telefoon",
        price=300,
        quantity=9,
        owner=kees,
    )

    ProductTag.create(product=computer, tag=tag_desktop)
    ProductTag.create(product=dvd_player, tag=tag_video)
    ProductTag.create(product=dvd_player, tag=tag_audio)
    ProductTag.create(product=cd_player, tag=tag_audio)
    ProductTag.create(product=ipad, tag=tag_apple)
    ProductTag.create(product=ipad, tag=tag_tablet)
    ProductTag.create(product=iphone, tag=tag_apple)
    ProductTag.create(product=iphone, tag=tag_phone)
    ProductTag.create(product=samsung, tag=tag_samsung)
    ProductTag.create(product=samsung, tag=tag_phone)

    db.close


populate_test_data()
