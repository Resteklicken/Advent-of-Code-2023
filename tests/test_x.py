import pytest

from aoc import INPUT_DIR
from aoc.day_x import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/x_1_test.txt", "r", encoding="utf-8") as f:
        return f.readlines()
