"""Tests for test module 1113 — covers src modules [4449, 4450, 4451, 4452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4449 import add_4449
from module_4450 import subtract_4450
from module_4451 import multiply_4451
from module_4452 import divide_4452

def test_add_4449():
    assert add_4449(2, 3) == 5

def test_subtract_4450():
    assert subtract_4450(10, 4) == 6

def test_multiply_4451():
    assert multiply_4451(3, 7) == 21

def test_divide_4452():
    assert divide_4452(10, 2) == 5.0
