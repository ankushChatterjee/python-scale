"""Tests for test module 335 — covers src modules [1337, 1338, 1339, 1340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1337 import add_1337
from module_1338 import subtract_1338
from module_1339 import multiply_1339
from module_1340 import divide_1340

def test_add_1337():
    assert add_1337(2, 3) == 5

def test_subtract_1338():
    assert subtract_1338(10, 4) == 6

def test_multiply_1339():
    assert multiply_1339(3, 7) == 21

def test_divide_1340():
    assert divide_1340(10, 2) == 5.0
