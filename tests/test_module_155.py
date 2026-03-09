"""Tests for test module 155 — covers src modules [617, 618, 619, 620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_617 import add_617
from module_618 import subtract_618
from module_619 import multiply_619
from module_620 import divide_620

def test_add_617():
    assert add_617(2, 3) == 5

def test_subtract_618():
    assert subtract_618(10, 4) == 6

def test_multiply_619():
    assert multiply_619(3, 7) == 21

def test_divide_620():
    assert divide_620(10, 2) == 5.0
