class Product:
    """Класс создания экземпляра продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Функция инициализации"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
