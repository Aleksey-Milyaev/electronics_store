class Category:
    """Класс создания экземпляра категории"""

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """Функция инициализации"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len([x for x in products])
