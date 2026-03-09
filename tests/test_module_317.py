"""Tests for test module 317 — covers src modules [1265, 1266, 1267, 1268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1265 import add_1265
from module_1266 import subtract_1266
from module_1267 import multiply_1267
from module_1268 import divide_1268

def test_add_1265():
    assert add_1265(2, 3) == 5

def test_subtract_1266():
    assert subtract_1266(10, 4) == 6

def test_multiply_1267():
    assert multiply_1267(3, 7) == 21

def test_divide_1268():
    assert divide_1268(10, 2) == 5.0
