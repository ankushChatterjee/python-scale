"""Tests for test module 957 — covers src modules [3825, 3826, 3827, 3828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3825 import add_3825
from module_3826 import subtract_3826
from module_3827 import multiply_3827
from module_3828 import divide_3828

def test_add_3825():
    assert add_3825(2, 3) == 5

def test_subtract_3826():
    assert subtract_3826(10, 4) == 6

def test_multiply_3827():
    assert multiply_3827(3, 7) == 21

def test_divide_3828():
    assert divide_3828(10, 2) == 5.0
