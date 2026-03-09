"""Tests for test module 1337 — covers src modules [5345, 5346, 5347, 5348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5345 import add_5345
from module_5346 import subtract_5346
from module_5347 import multiply_5347
from module_5348 import divide_5348

def test_add_5345():
    assert add_5345(2, 3) == 5

def test_subtract_5346():
    assert subtract_5346(10, 4) == 6

def test_multiply_5347():
    assert multiply_5347(3, 7) == 21

def test_divide_5348():
    assert divide_5348(10, 2) == 5.0
