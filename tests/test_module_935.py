"""Tests for test module 935 — covers src modules [3737, 3738, 3739, 3740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3737 import add_3737
from module_3738 import subtract_3738
from module_3739 import multiply_3739
from module_3740 import divide_3740

def test_add_3737():
    assert add_3737(2, 3) == 5

def test_subtract_3738():
    assert subtract_3738(10, 4) == 6

def test_multiply_3739():
    assert multiply_3739(3, 7) == 21

def test_divide_3740():
    assert divide_3740(10, 2) == 5.0
