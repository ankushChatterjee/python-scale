"""Tests for test module 393 — covers src modules [1569, 1570, 1571, 1572]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1569 import add_1569
from module_1570 import subtract_1570
from module_1571 import multiply_1571
from module_1572 import divide_1572

def test_add_1569():
    assert add_1569(2, 3) == 5

def test_subtract_1570():
    assert subtract_1570(10, 4) == 6

def test_multiply_1571():
    assert multiply_1571(3, 7) == 21

def test_divide_1572():
    assert divide_1572(10, 2) == 5.0
