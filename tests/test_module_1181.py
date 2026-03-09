"""Tests for test module 1181 — covers src modules [4721, 4722, 4723, 4724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4721 import add_4721
from module_4722 import subtract_4722
from module_4723 import multiply_4723
from module_4724 import divide_4724

def test_add_4721():
    assert add_4721(2, 3) == 5

def test_subtract_4722():
    assert subtract_4722(10, 4) == 6

def test_multiply_4723():
    assert multiply_4723(3, 7) == 21

def test_divide_4724():
    assert divide_4724(10, 2) == 5.0
