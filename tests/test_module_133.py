"""Tests for test module 133 — covers src modules [529, 530, 531, 532]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_529 import add_529
from module_530 import subtract_530
from module_531 import multiply_531
from module_532 import divide_532

def test_add_529():
    assert add_529(2, 3) == 5

def test_subtract_530():
    assert subtract_530(10, 4) == 6

def test_multiply_531():
    assert multiply_531(3, 7) == 21

def test_divide_532():
    assert divide_532(10, 2) == 5.0
