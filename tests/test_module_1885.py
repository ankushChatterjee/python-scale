"""Tests for test module 1885 — covers src modules [7537, 7538, 7539, 7540]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7537 import add_7537
from module_7538 import subtract_7538
from module_7539 import multiply_7539
from module_7540 import divide_7540

def test_add_7537():
    assert add_7537(2, 3) == 5

def test_subtract_7538():
    assert subtract_7538(10, 4) == 6

def test_multiply_7539():
    assert multiply_7539(3, 7) == 21

def test_divide_7540():
    assert divide_7540(10, 2) == 5.0
