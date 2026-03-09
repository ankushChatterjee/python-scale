"""Tests for test module 181 — covers src modules [721, 722, 723, 724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_721 import add_721
from module_722 import subtract_722
from module_723 import multiply_723
from module_724 import divide_724

def test_add_721():
    assert add_721(2, 3) == 5

def test_subtract_722():
    assert subtract_722(10, 4) == 6

def test_multiply_723():
    assert multiply_723(3, 7) == 21

def test_divide_724():
    assert divide_724(10, 2) == 5.0
