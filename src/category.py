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
        self.__products = products
        Category.category_count += 1
        Category.product_count += len([x for x in products])

    def add_product(self, product: list):
        name_list = []
        for pr in self.__products:
            name_list.append(pr.name)
        if product.name in name_list:
            for pro in self.__products:
                if pro.name == product.name:
                    pro.quantity += product.quantity
        else:
            self.__products.append(product)
            self.product_count += 1

    @property
    def products(self):
        products_str = ''
        for pr in self.__products:
            products_str += f"{pr.name}, {pr.price} руб. Остаток: {pr.quantity} шт.\n"
        return products_str

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."
