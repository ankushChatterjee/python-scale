"""Tests for test module 1137 — covers src modules [4545, 4546, 4547, 4548]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4545 import add_4545
from module_4546 import subtract_4546
from module_4547 import multiply_4547
from module_4548 import divide_4548

def test_add_4545():
    assert add_4545(2, 3) == 5

def test_subtract_4546():
    assert subtract_4546(10, 4) == 6

def test_multiply_4547():
    assert multiply_4547(3, 7) == 21

def test_divide_4548():
    assert divide_4548(10, 2) == 5.0
