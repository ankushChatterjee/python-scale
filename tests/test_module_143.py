"""Tests for test module 143 — covers src modules [569, 570, 571, 572]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_569 import add_569
from module_570 import subtract_570
from module_571 import multiply_571
from module_572 import divide_572

def test_add_569():
    assert add_569(2, 3) == 5

def test_subtract_570():
    assert subtract_570(10, 4) == 6

def test_multiply_571():
    assert multiply_571(3, 7) == 21

def test_divide_572():
    assert divide_572(10, 2) == 5.0
