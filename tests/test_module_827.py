"""Tests for test module 827 — covers src modules [3305, 3306, 3307, 3308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3305 import add_3305
from module_3306 import subtract_3306
from module_3307 import multiply_3307
from module_3308 import divide_3308

def test_add_3305():
    assert add_3305(2, 3) == 5

def test_subtract_3306():
    assert subtract_3306(10, 4) == 6

def test_multiply_3307():
    assert multiply_3307(3, 7) == 21

def test_divide_3308():
    assert divide_3308(10, 2) == 5.0
