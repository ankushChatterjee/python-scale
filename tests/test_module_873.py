"""Tests for test module 873 — covers src modules [3489, 3490, 3491, 3492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3489 import add_3489
from module_3490 import subtract_3490
from module_3491 import multiply_3491
from module_3492 import divide_3492

def test_add_3489():
    assert add_3489(2, 3) == 5

def test_subtract_3490():
    assert subtract_3490(10, 4) == 6

def test_multiply_3491():
    assert multiply_3491(3, 7) == 21

def test_divide_3492():
    assert divide_3492(10, 2) == 5.0
