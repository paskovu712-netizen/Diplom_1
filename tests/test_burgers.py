import pytest
from unittest.mock import Mock

from practikum.burger import Burger
from practikum.bun import Bun
from practikum.ingredient import Ingredient

# Подготовка тестовых данных
bun_mock = Mock(spec=Bun)
bun_mock.get_name.return_value = "test_bun"
bun_mock.get_price.return_value = 100.0

ingredient_mock = Mock(spec=Ingredient)
ingredient_mock.get_name.return_value = "test_ingredient"
ingredient_mock.get_type.return_value = "FILLING"
ingredient_mock.get_price.return_value = 50.0

@pytest.fixture
def burger_with_bun():
    burger = Burger()
    burger.set_buns(bun_mock)
    return burger

@pytest.fixture
def burger_with_ingredients():
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    return burger

# Тестирование базовых методов
def test_init_burger(empty_burger):
    assert empty_burger.bun is None
    assert empty_burger.ingredients == []

def test_set_buns(empty_burger):
    empty_burger.set_buns(bun_mock)
    assert empty_burger.bun == bun_mock

# Параметризованные тесты для добавления ингредиентов
@pytest.mark.parametrize("ingredient_count", [1, 2, 3, 5])
def test_add_ingredients(burger_with_bun, ingredient_count):
    for _ in range(ingredient_count):
        burger_with_bun.add_ingredient(ingredient_mock)
    assert len(burger_with_bun.ingredients) == ingredient_count

# Тестирование удаления ингредиентов
def test_remove_ingredient(burger_with_ingredients):
    initial_length = len(burger_with_ingredients.ingredients)
    burger_with_ingredients.remove_ingredient(0)
    assert len(burger_with_ingredients.ingredients) == initial_length - 1

# Тестирование перемещения ингредиентов
def test_move_ingredient(burger_with_ingredients):
    burger_with_ingredients.add_ingredient(ingredient_mock)
    burger_with_ingredients.move_ingredient(0, 1)
    assert burger_with_ingredients.ingredients[1] == ingredient_mock

# Тестирование расчета цены
def test_get_price(burger_with_ingredients):
    expected_price = bun_mock.get_price() * 2 + ingredient_mock.get_price()
    assert burger_with_ingredients.get_price() == expected_price

# Тестирование формирования рецепта
def test_get_receipt(burger_with_ingredients):
    receipt = burger_with_ingredients.get_receipt()
    assert bun_mock.get_name() in receipt
    assert ingredient_mock.get_name() in receipt
    assert str(burger_with_ingredients.get_price()) in receipt

# Тесты на исключения
def test_remove_invalid_index(burger_with_bun):
    with pytest.raises(IndexError):
        burger_with_bun.remove_ingredient(0)

def test_move_invalid_index(burger_with_bun):
    with pytest.raises(IndexError):
        burger_with_bun.move_ingredient(0, 1)
