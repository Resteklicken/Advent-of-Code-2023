import pytest

from aoc import INPUT_DIR
from aoc.day_6 import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/6_1_test.txt", "r", encoding="utf-8") as f:
        return f.readlines()
