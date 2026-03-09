"""Tests for test module 893 — covers src modules [3569, 3570, 3571, 3572]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3569 import add_3569
from module_3570 import subtract_3570
from module_3571 import multiply_3571
from module_3572 import divide_3572

def test_add_3569():
    assert add_3569(2, 3) == 5

def test_subtract_3570():
    assert subtract_3570(10, 4) == 6

def test_multiply_3571():
    assert multiply_3571(3, 7) == 21

def test_divide_3572():
    assert divide_3572(10, 2) == 5.0
