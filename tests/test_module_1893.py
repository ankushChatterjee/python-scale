"""Tests for test module 1893 — covers src modules [7569, 7570, 7571, 7572]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7569 import add_7569
from module_7570 import subtract_7570
from module_7571 import multiply_7571
from module_7572 import divide_7572

def test_add_7569():
    assert add_7569(2, 3) == 5

def test_subtract_7570():
    assert subtract_7570(10, 4) == 6

def test_multiply_7571():
    assert multiply_7571(3, 7) == 21

def test_divide_7572():
    assert divide_7572(10, 2) == 5.0
