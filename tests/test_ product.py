from typing import Any

import pytest

from src.product import Product


@pytest.fixture
def get_product() -> Any:
    return Product("name", "product info", 10000, 5)


def test_category_init(get_product: Any) -> Any:
    assert get_product.name == "name"
    assert get_product.description == "product info"
    assert get_product.price == 10000
    assert get_product.quantity == 5
