"""Tests for test module 445 — covers src modules [1777, 1778, 1779, 1780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1777 import add_1777
from module_1778 import subtract_1778
from module_1779 import multiply_1779
from module_1780 import divide_1780

def test_add_1777():
    assert add_1777(2, 3) == 5

def test_subtract_1778():
    assert subtract_1778(10, 4) == 6

def test_multiply_1779():
    assert multiply_1779(3, 7) == 21

def test_divide_1780():
    assert divide_1780(10, 2) == 5.0
