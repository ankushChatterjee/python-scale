"""Tests for test module 2107 — covers src modules [8425, 8426, 8427, 8428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8425 import add_8425
from module_8426 import subtract_8426
from module_8427 import multiply_8427
from module_8428 import divide_8428

def test_add_8425():
    assert add_8425(2, 3) == 5

def test_subtract_8426():
    assert subtract_8426(10, 4) == 6

def test_multiply_8427():
    assert multiply_8427(3, 7) == 21

def test_divide_8428():
    assert divide_8428(10, 2) == 5.0
