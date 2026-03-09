"""Tests for test module 787 — covers src modules [3145, 3146, 3147, 3148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3145 import add_3145
from module_3146 import subtract_3146
from module_3147 import multiply_3147
from module_3148 import divide_3148

def test_add_3145():
    assert add_3145(2, 3) == 5

def test_subtract_3146():
    assert subtract_3146(10, 4) == 6

def test_multiply_3147():
    assert multiply_3147(3, 7) == 21

def test_divide_3148():
    assert divide_3148(10, 2) == 5.0
