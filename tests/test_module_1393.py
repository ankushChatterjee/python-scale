"""Tests for test module 1393 — covers src modules [5569, 5570, 5571, 5572]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5569 import add_5569
from module_5570 import subtract_5570
from module_5571 import multiply_5571
from module_5572 import divide_5572

def test_add_5569():
    assert add_5569(2, 3) == 5

def test_subtract_5570():
    assert subtract_5570(10, 4) == 6

def test_multiply_5571():
    assert multiply_5571(3, 7) == 21

def test_divide_5572():
    assert divide_5572(10, 2) == 5.0
