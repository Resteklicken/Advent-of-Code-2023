import pytest

from aoc import INPUT_DIR
from aoc.day_2 import *


@pytest.fixture
def test_input_1():
    with open(f"{INPUT_DIR}/2_1_test.txt") as f:
        return f.readlines()
