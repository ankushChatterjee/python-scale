"""Tests for test module 1133 — covers src modules [4529, 4530, 4531, 4532]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4529 import add_4529
from module_4530 import subtract_4530
from module_4531 import multiply_4531
from module_4532 import divide_4532

def test_add_4529():
    assert add_4529(2, 3) == 5

def test_subtract_4530():
    assert subtract_4530(10, 4) == 6

def test_multiply_4531():
    assert multiply_4531(3, 7) == 21

def test_divide_4532():
    assert divide_4532(10, 2) == 5.0
