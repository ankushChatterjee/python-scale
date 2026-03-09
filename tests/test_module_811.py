"""Tests for test module 811 — covers src modules [3241, 3242, 3243, 3244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3241 import add_3241
from module_3242 import subtract_3242
from module_3243 import multiply_3243
from module_3244 import divide_3244

def test_add_3241():
    assert add_3241(2, 3) == 5

def test_subtract_3242():
    assert subtract_3242(10, 4) == 6

def test_multiply_3243():
    assert multiply_3243(3, 7) == 21

def test_divide_3244():
    assert divide_3244(10, 2) == 5.0
