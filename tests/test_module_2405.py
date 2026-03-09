"""Tests for test module 2405 — covers src modules [9617, 9618, 9619, 9620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9617 import add_9617
from module_9618 import subtract_9618
from module_9619 import multiply_9619
from module_9620 import divide_9620

def test_add_9617():
    assert add_9617(2, 3) == 5

def test_subtract_9618():
    assert subtract_9618(10, 4) == 6

def test_multiply_9619():
    assert multiply_9619(3, 7) == 21

def test_divide_9620():
    assert divide_9620(10, 2) == 5.0
