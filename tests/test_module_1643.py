"""Tests for test module 1643 — covers src modules [6569, 6570, 6571, 6572]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6569 import add_6569
from module_6570 import subtract_6570
from module_6571 import multiply_6571
from module_6572 import divide_6572

def test_add_6569():
    assert add_6569(2, 3) == 5

def test_subtract_6570():
    assert subtract_6570(10, 4) == 6

def test_multiply_6571():
    assert multiply_6571(3, 7) == 21

def test_divide_6572():
    assert divide_6572(10, 2) == 5.0
