"""Tests for test module 579 — covers src modules [2313, 2314, 2315, 2316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2313 import add_2313
from module_2314 import subtract_2314
from module_2315 import multiply_2315
from module_2316 import divide_2316

def test_add_2313():
    assert add_2313(2, 3) == 5

def test_subtract_2314():
    assert subtract_2314(10, 4) == 6

def test_multiply_2315():
    assert multiply_2315(3, 7) == 21

def test_divide_2316():
    assert divide_2316(10, 2) == 5.0
