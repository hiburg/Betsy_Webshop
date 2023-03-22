from models import *

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


def search(term):
    products = Product.select().where(
        Product.name.contains(term) | Product.description.contains(term)
    )
    print(f"The search on '{term}' delivers these products:")
    print("========================================================")
    if len(products) == 0:
        print("<< No products were found >>")
    else:
        for product in products:
            print(
                f"Productname: {product.name}  Price: {product.price}  Quantity: {product.quantity}"
            )


def list_user_products(user_id):
    try:
        owner = User.get_by_id(user_id)
        print(f"User: '{owner.username}' has the following products:")
        print("========================================================")
        for product in owner.products:
            print(
                f"Productname: {product.name}  Price: {product.price}  Quantity: {product.quantity}"
            )
    except DoesNotExist:
        print(f"<< No products were found for user_id: '{user_id}' >>")


def list_products_per_tag(tag_id):
    try:
        tag = Tag.get_by_id(tag_id)
    except DoesNotExist:
        print(f"Tag_id: '{tag_id}' was not found")
        return

    print(f"Tag '{tag.name}' is present in the following products:")
    print("=======================================================")
    products = Product.select().join(ProductTag).where(ProductTag.tag == tag_id)
    for product in products:
        print(product.product_id, "|", product.name, "|", product.description)


def add_product_to_catalog(user_id, product):
    Product.create(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
        owner=user_id,
    )
    print(
        f"Product: '{product.name}' has been added. Owner is: {User.get_by_id(user_id).username}"
    )


def update_stock(product_id, new_quantity):
    num_upd = Product.set_by_id(product_id, {"quantity": new_quantity})
    if num_upd == 0:
        print(f"Product with id: '{product_id}' is not present")
    else:
        print(
            f"Product with id: '{product_id}' has been updated, new quantity is: {new_quantity}"
        )


def purchase_product(product_id, buyer_id, quantity):
    try:
        product = Product.get_by_id(product_id)
    except DoesNotExist:
        print(f"Product with id: '{product_id}' is not present")
        return

    try:
        user = User.get_by_id(buyer_id)
    except DoesNotExist:
        print(f"Buyer with id: '{buyer_id}' is not present")
        return

    if product.quantity >= quantity:
        new_quantity = product.quantity - quantity
        update_stock(product_id, new_quantity)
        Transaction.create(buyer=user, product_bought=product, quantity_bought=quantity)
        print(
            f"Product with id: '{product_id}' has been sold to '{user.username}', transaction has been added"
        )
    else:
        print(
            f"Product with id: '{product_id}' is not in stock, the current quantity is: {product.quantity}"
        )


def remove_product(product_id):
    try:
        product = Product.get_by_id(product_id)
    except DoesNotExist:
        print(f"Product with id: '{product_id}' is not present")
        return

    product.delete_instance(recursive=True, delete_nullable=True)
    print(f"Product with id: '{product_id}' has been deleted")


# Voor testdoeleinden en gemak bij controle van de assignment, heb ik  de onderstaande
# def main() maar laten staan.
def main():
    # search("Tablet")
    # search("iphone")
    # search("iPhOnE")
    # search("i")
    # search("nieuw")
    # search("pC")

    # list_user_products(2)

    # list_products_per_tag(1)

    # piet = User.get_by_id(3)
    # product_temp = Product(name="Nokia3330", description="Een 2e hands Nokia uit 2008", price=20.56789, quantity=999, owner=piet)
    # add_product_to_catalog(1, product_temp)

    # update_stock(3, 900)

    # purchase_product(7,3,20)

    # remove_product(4)
    pass


if __name__ == "__main__":
    main()
