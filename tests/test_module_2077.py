"""Tests for test module 2077 — covers src modules [8305, 8306, 8307, 8308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8305 import add_8305
from module_8306 import subtract_8306
from module_8307 import multiply_8307
from module_8308 import divide_8308

def test_add_8305():
    assert add_8305(2, 3) == 5

def test_subtract_8306():
    assert subtract_8306(10, 4) == 6

def test_multiply_8307():
    assert multiply_8307(3, 7) == 21

def test_divide_8308():
    assert divide_8308(10, 2) == 5.0
