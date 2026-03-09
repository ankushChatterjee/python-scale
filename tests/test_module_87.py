"""Tests for test module 87 — covers src modules [345, 346, 347, 348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_345 import add_345
from module_346 import subtract_346
from module_347 import multiply_347
from module_348 import divide_348

def test_add_345():
    assert add_345(2, 3) == 5

def test_subtract_346():
    assert subtract_346(10, 4) == 6

def test_multiply_347():
    assert multiply_347(3, 7) == 21

def test_divide_348():
    assert divide_348(10, 2) == 5.0
