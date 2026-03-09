"""Tests for test module 339 — covers src modules [1353, 1354, 1355, 1356]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1353 import add_1353
from module_1354 import subtract_1354
from module_1355 import multiply_1355
from module_1356 import divide_1356

def test_add_1353():
    assert add_1353(2, 3) == 5

def test_subtract_1354():
    assert subtract_1354(10, 4) == 6

def test_multiply_1355():
    assert multiply_1355(3, 7) == 21

def test_divide_1356():
    assert divide_1356(10, 2) == 5.0
