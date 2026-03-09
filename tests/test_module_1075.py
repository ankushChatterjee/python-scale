"""Tests for test module 1075 — covers src modules [4297, 4298, 4299, 4300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4297 import add_4297
from module_4298 import subtract_4298
from module_4299 import multiply_4299
from module_4300 import divide_4300

def test_add_4297():
    assert add_4297(2, 3) == 5

def test_subtract_4298():
    assert subtract_4298(10, 4) == 6

def test_multiply_4299():
    assert multiply_4299(3, 7) == 21

def test_divide_4300():
    assert divide_4300(10, 2) == 5.0
