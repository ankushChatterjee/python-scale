"""Tests for test module 333 — covers src modules [1329, 1330, 1331, 1332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1329 import add_1329
from module_1330 import subtract_1330
from module_1331 import multiply_1331
from module_1332 import divide_1332

def test_add_1329():
    assert add_1329(2, 3) == 5

def test_subtract_1330():
    assert subtract_1330(10, 4) == 6

def test_multiply_1331():
    assert multiply_1331(3, 7) == 21

def test_divide_1332():
    assert divide_1332(10, 2) == 5.0
