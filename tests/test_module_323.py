"""Tests for test module 323 — covers src modules [1289, 1290, 1291, 1292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1289 import add_1289
from module_1290 import subtract_1290
from module_1291 import multiply_1291
from module_1292 import divide_1292

def test_add_1289():
    assert add_1289(2, 3) == 5

def test_subtract_1290():
    assert subtract_1290(10, 4) == 6

def test_multiply_1291():
    assert multiply_1291(3, 7) == 21

def test_divide_1292():
    assert divide_1292(10, 2) == 5.0
