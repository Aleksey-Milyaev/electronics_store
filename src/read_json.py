import json
import os

from src.category import Category
from src.product import Product


def get_product_category() -> list:
    """Функция чтения данных из json файла"""
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")

    with open(path, encoding="UTF8") as file:
        content = json.load(file)

        list_category = []
        for category in content:
            new_category = Category(category["name"], category["description"], products=[])
            for product in category["products"]:
                new_category.products.append(
                    Product(product["name"], product["description"], product["price"], product["quantity"])
                )
            list_category.append(new_category)

        return list_category
