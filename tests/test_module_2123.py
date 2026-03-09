"""Tests for test module 2123 — covers src modules [8489, 8490, 8491, 8492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8489 import add_8489
from module_8490 import subtract_8490
from module_8491 import multiply_8491
from module_8492 import divide_8492

def test_add_8489():
    assert add_8489(2, 3) == 5

def test_subtract_8490():
    assert subtract_8490(10, 4) == 6

def test_multiply_8491():
    assert multiply_8491(3, 7) == 21

def test_divide_8492():
    assert divide_8492(10, 2) == 5.0
