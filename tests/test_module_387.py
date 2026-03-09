"""Tests for test module 387 — covers src modules [1545, 1546, 1547, 1548]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1545 import add_1545
from module_1546 import subtract_1546
from module_1547 import multiply_1547
from module_1548 import divide_1548

def test_add_1545():
    assert add_1545(2, 3) == 5

def test_subtract_1546():
    assert subtract_1546(10, 4) == 6

def test_multiply_1547():
    assert multiply_1547(3, 7) == 21

def test_divide_1548():
    assert divide_1548(10, 2) == 5.0
