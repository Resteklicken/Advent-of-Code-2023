import pytest

from aoc import INPUT_DIR
from aoc.day_5 import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/5_1_test.txt", "r", encoding="utf-8") as f:
        return f.readlines()
