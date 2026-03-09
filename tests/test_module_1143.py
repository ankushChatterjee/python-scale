"""Tests for test module 1143 — covers src modules [4569, 4570, 4571, 4572]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4569 import add_4569
from module_4570 import subtract_4570
from module_4571 import multiply_4571
from module_4572 import divide_4572

def test_add_4569():
    assert add_4569(2, 3) == 5

def test_subtract_4570():
    assert subtract_4570(10, 4) == 6

def test_multiply_4571():
    assert multiply_4571(3, 7) == 21

def test_divide_4572():
    assert divide_4572(10, 2) == 5.0
