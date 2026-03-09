"""Tests for test module 2137 — covers src modules [8545, 8546, 8547, 8548]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8545 import add_8545
from module_8546 import subtract_8546
from module_8547 import multiply_8547
from module_8548 import divide_8548

def test_add_8545():
    assert add_8545(2, 3) == 5

def test_subtract_8546():
    assert subtract_8546(10, 4) == 6

def test_multiply_8547():
    assert multiply_8547(3, 7) == 21

def test_divide_8548():
    assert divide_8548(10, 2) == 5.0
