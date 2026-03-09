"""Tests for test module 905 — covers src modules [3617, 3618, 3619, 3620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3617 import add_3617
from module_3618 import subtract_3618
from module_3619 import multiply_3619
from module_3620 import divide_3620

def test_add_3617():
    assert add_3617(2, 3) == 5

def test_subtract_3618():
    assert subtract_3618(10, 4) == 6

def test_multiply_3619():
    assert multiply_3619(3, 7) == 21

def test_divide_3620():
    assert divide_3620(10, 2) == 5.0
