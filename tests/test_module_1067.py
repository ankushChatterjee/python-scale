"""Tests for test module 1067 — covers src modules [4265, 4266, 4267, 4268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4265 import add_4265
from module_4266 import subtract_4266
from module_4267 import multiply_4267
from module_4268 import divide_4268

def test_add_4265():
    assert add_4265(2, 3) == 5

def test_subtract_4266():
    assert subtract_4266(10, 4) == 6

def test_multiply_4267():
    assert multiply_4267(3, 7) == 21

def test_divide_4268():
    assert divide_4268(10, 2) == 5.0
