"""Tests for test module 2393 — covers src modules [9569, 9570, 9571, 9572]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9569 import add_9569
from module_9570 import subtract_9570
from module_9571 import multiply_9571
from module_9572 import divide_9572

def test_add_9569():
    assert add_9569(2, 3) == 5

def test_subtract_9570():
    assert subtract_9570(10, 4) == 6

def test_multiply_9571():
    assert multiply_9571(3, 7) == 21

def test_divide_9572():
    assert divide_9572(10, 2) == 5.0
