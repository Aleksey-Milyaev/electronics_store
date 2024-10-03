from typing import Any

import pytest

from src.category import Category


@pytest.fixture
def get_category() -> Any:
    return Category("category", "category info", ["one", "two"])


def test_category_init(get_category: Any) -> Any:
    assert get_category.name == "category"
    assert get_category.description == "category info"
    assert get_category.products == ["one", "two"]
    assert get_category.category_count == 1
    assert get_category.product_count == 2
