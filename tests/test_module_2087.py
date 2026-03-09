"""Tests for test module 2087 — covers src modules [8345, 8346, 8347, 8348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8345 import add_8345
from module_8346 import subtract_8346
from module_8347 import multiply_8347
from module_8348 import divide_8348

def test_add_8345():
    assert add_8345(2, 3) == 5

def test_subtract_8346():
    assert subtract_8346(10, 4) == 6

def test_multiply_8347():
    assert multiply_8347(3, 7) == 21

def test_divide_8348():
    assert divide_8348(10, 2) == 5.0
