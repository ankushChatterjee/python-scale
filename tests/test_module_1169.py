"""Tests for test module 1169 — covers src modules [4673, 4674, 4675, 4676]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4673 import add_4673
from module_4674 import subtract_4674
from module_4675 import multiply_4675
from module_4676 import divide_4676

def test_add_4673():
    assert add_4673(2, 3) == 5

def test_subtract_4674():
    assert subtract_4674(10, 4) == 6

def test_multiply_4675():
    assert multiply_4675(3, 7) == 21

def test_divide_4676():
    assert divide_4676(10, 2) == 5.0
