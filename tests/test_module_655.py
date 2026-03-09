"""Tests for test module 655 — covers src modules [2617, 2618, 2619, 2620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2617 import add_2617
from module_2618 import subtract_2618
from module_2619 import multiply_2619
from module_2620 import divide_2620

def test_add_2617():
    assert add_2617(2, 3) == 5

def test_subtract_2618():
    assert subtract_2618(10, 4) == 6

def test_multiply_2619():
    assert multiply_2619(3, 7) == 21

def test_divide_2620():
    assert divide_2620(10, 2) == 5.0
