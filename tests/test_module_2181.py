"""Tests for test module 2181 — covers src modules [8721, 8722, 8723, 8724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8721 import add_8721
from module_8722 import subtract_8722
from module_8723 import multiply_8723
from module_8724 import divide_8724

def test_add_8721():
    assert add_8721(2, 3) == 5

def test_subtract_8722():
    assert subtract_8722(10, 4) == 6

def test_multiply_8723():
    assert multiply_8723(3, 7) == 21

def test_divide_8724():
    assert divide_8724(10, 2) == 5.0
