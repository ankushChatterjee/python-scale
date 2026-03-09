"""Tests for test module 577 — covers src modules [2305, 2306, 2307, 2308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2305 import add_2305
from module_2306 import subtract_2306
from module_2307 import multiply_2307
from module_2308 import divide_2308

def test_add_2305():
    assert add_2305(2, 3) == 5

def test_subtract_2306():
    assert subtract_2306(10, 4) == 6

def test_multiply_2307():
    assert multiply_2307(3, 7) == 21

def test_divide_2308():
    assert divide_2308(10, 2) == 5.0
