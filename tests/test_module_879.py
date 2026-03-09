"""Tests for test module 879 — covers src modules [3513, 3514, 3515, 3516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3513 import add_3513
from module_3514 import subtract_3514
from module_3515 import multiply_3515
from module_3516 import divide_3516

def test_add_3513():
    assert add_3513(2, 3) == 5

def test_subtract_3514():
    assert subtract_3514(10, 4) == 6

def test_multiply_3515():
    assert multiply_3515(3, 7) == 21

def test_divide_3516():
    assert divide_3516(10, 2) == 5.0
