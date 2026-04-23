import pytest

class TestBurger:
    def test_init_burger(self, empty_burger):
        assert empty_burger.bun is None
        assert empty_burger.ingredients == []

    def test_set_buns(self, empty_burger, bun_mock):
        empty_burger.set_buns(bun_mock)
        assert empty_burger.bun == bun_mock

    # Параметризованные тесты для добавления ингредиентов
    @pytest.mark.parametrize("ingredient_count", [1, 2, 3, 5])
    def test_add_ingredients(self, burger_with_bun, ingredient_mock, ingredient_count):
        for _ in range(ingredient_count):
            burger_with_bun.add_ingredient(ingredient_mock)
        assert len(burger_with_bun.ingredients) == ingredient_count

    # Тестирование удаления ингредиентов
    def test_remove_ingredient(self, burger_with_ingredients):
        initial_length = len(burger_with_ingredients.ingredients)
        burger_with_ingredients.remove_ingredient(0)
        assert len(burger_with_ingredients.ingredients) == initial_length - 1

    # Тестирование перемещения ингредиентов
    def test_move_ingredient(self, burger_with_ingredients, ingredient_mock):
        burger_with_ingredients.add_ingredient(ingredient_mock)
        burger_with_ingredients.move_ingredient(0, 1)
        assert burger_with_ingredients.ingredients[1] == ingredient_mock

    # Тестирование расчета цены
    def test_get_price(self, burger_with_ingredients, bun_mock, ingredient_mock):
        expected_price = bun_mock.get_price() * 2 + ingredient_mock.get_price()
        assert burger_with_ingredients.get_price() == expected_price

    # Тестирование формирования рецепта
    def test_get_receipt(self, burger_with_ingredients, bun_mock, ingredient_mock):
        receipt = burger_with_ingredients.get_receipt()
        assert bun_mock.get_name() in receipt
        assert ingredient_mock.get_name() in receipt
        assert str(burger_with_ingredients.get_price()) in receipt

    # Тесты на исключения
    def test_remove_invalid_index(self, burger_with_bun):
        with pytest.raises(IndexError):
            burger_with_bun.remove_ingredient(0)

    def test_move_invalid_index(self, burger_with_bun):
        with pytest.raises(IndexError):
            burger_with_bun.move_ingredient(0, 1)
