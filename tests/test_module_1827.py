"""Tests for test module 1827 — covers src modules [7305, 7306, 7307, 7308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7305 import add_7305
from module_7306 import subtract_7306
from module_7307 import multiply_7307
from module_7308 import divide_7308

def test_add_7305():
    assert add_7305(2, 3) == 5

def test_subtract_7306():
    assert subtract_7306(10, 4) == 6

def test_multiply_7307():
    assert multiply_7307(3, 7) == 21

def test_divide_7308():
    assert divide_7308(10, 2) == 5.0
