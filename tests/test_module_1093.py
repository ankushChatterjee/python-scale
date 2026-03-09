"""Tests for test module 1093 — covers src modules [4369, 4370, 4371, 4372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4369 import add_4369
from module_4370 import subtract_4370
from module_4371 import multiply_4371
from module_4372 import divide_4372

def test_add_4369():
    assert add_4369(2, 3) == 5

def test_subtract_4370():
    assert subtract_4370(10, 4) == 6

def test_multiply_4371():
    assert multiply_4371(3, 7) == 21

def test_divide_4372():
    assert divide_4372(10, 2) == 5.0
