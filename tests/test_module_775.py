"""Tests for test module 775 — covers src modules [3097, 3098, 3099, 3100]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3097 import add_3097
from module_3098 import subtract_3098
from module_3099 import multiply_3099
from module_3100 import divide_3100

def test_add_3097():
    assert add_3097(2, 3) == 5

def test_subtract_3098():
    assert subtract_3098(10, 4) == 6

def test_multiply_3099():
    assert multiply_3099(3, 7) == 21

def test_divide_3100():
    assert divide_3100(10, 2) == 5.0
