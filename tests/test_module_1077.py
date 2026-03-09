"""Tests for test module 1077 — covers src modules [4305, 4306, 4307, 4308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4305 import add_4305
from module_4306 import subtract_4306
from module_4307 import multiply_4307
from module_4308 import divide_4308

def test_add_4305():
    assert add_4305(2, 3) == 5

def test_subtract_4306():
    assert subtract_4306(10, 4) == 6

def test_multiply_4307():
    assert multiply_4307(3, 7) == 21

def test_divide_4308():
    assert divide_4308(10, 2) == 5.0
