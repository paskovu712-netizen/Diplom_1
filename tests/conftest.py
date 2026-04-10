import pytest

from practikum.burger import Burger

@pytest.fixture
def empty_burger():
    return Burger()
