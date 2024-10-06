from typing import Any

import pytest

from src.category import Category


@pytest.fixture
def get_category() -> Any:
    return Category("category", "category info", [{"name": "Samsung Galaxy S23 Ultra",
                                                   "description": "256GB, Серый цвет, 200MP камера",
                                                   "price": 180000.0,
                                                   "quantity": 5}])


def test_category_init(get_category: Any) -> Any:
    assert get_category.name == "category"
    assert get_category.description == "category info"

    assert get_category.category_count == 1
    assert get_category.product_count == 1
