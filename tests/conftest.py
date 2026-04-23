import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@pytest.fixture
def bun_mock():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_name.return_value = "test_bun"
    bun_mock.get_price.return_value = 100.0
    return bun_mock

@pytest.fixture
def ingredient_mock():
    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_name.return_value = "test_ingredient"
    ingredient_mock.get_type.return_value = "FILLING"
    ingredient_mock.get_price.return_value = 50.0
    return ingredient_mock

@pytest.fixture
def empty_burger():
    return Burger()

@pytest.fixture
def burger_with_bun(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    return burger

@pytest.fixture
def burger_with_ingredients(bun_mock, ingredient_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    return burger
