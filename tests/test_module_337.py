"""Tests for test module 337 — covers src modules [1345, 1346, 1347, 1348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1345 import add_1345
from module_1346 import subtract_1346
from module_1347 import multiply_1347
from module_1348 import divide_1348

def test_add_1345():
    assert add_1345(2, 3) == 5

def test_subtract_1346():
    assert subtract_1346(10, 4) == 6

def test_multiply_1347():
    assert multiply_1347(3, 7) == 21

def test_divide_1348():
    assert divide_1348(10, 2) == 5.0
