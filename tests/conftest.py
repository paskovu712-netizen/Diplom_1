import pytest

from praktikum.burger import Burger

@pytest.fixture
def empty_burger():
    return Burger()
