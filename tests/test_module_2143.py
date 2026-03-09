"""Tests for test module 2143 — covers src modules [8569, 8570, 8571, 8572]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8569 import add_8569
from module_8570 import subtract_8570
from module_8571 import multiply_8571
from module_8572 import divide_8572

def test_add_8569():
    assert add_8569(2, 3) == 5

def test_subtract_8570():
    assert subtract_8570(10, 4) == 6

def test_multiply_8571():
    assert multiply_8571(3, 7) == 21

def test_divide_8572():
    assert divide_8572(10, 2) == 5.0
