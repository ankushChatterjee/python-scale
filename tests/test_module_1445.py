"""Tests for test module 1445 — covers src modules [5777, 5778, 5779, 5780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5777 import add_5777
from module_5778 import subtract_5778
from module_5779 import multiply_5779
from module_5780 import divide_5780

def test_add_5777():
    assert add_5777(2, 3) == 5

def test_subtract_5778():
    assert subtract_5778(10, 4) == 6

def test_multiply_5779():
    assert multiply_5779(3, 7) == 21

def test_divide_5780():
    assert divide_5780(10, 2) == 5.0
