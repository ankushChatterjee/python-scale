"""Tests for test module 2155 — covers src modules [8617, 8618, 8619, 8620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8617 import add_8617
from module_8618 import subtract_8618
from module_8619 import multiply_8619
from module_8620 import divide_8620

def test_add_8617():
    assert add_8617(2, 3) == 5

def test_subtract_8618():
    assert subtract_8618(10, 4) == 6

def test_multiply_8619():
    assert multiply_8619(3, 7) == 21

def test_divide_8620():
    assert divide_8620(10, 2) == 5.0
