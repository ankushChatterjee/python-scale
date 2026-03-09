"""Tests for test module 201 — covers src modules [801, 802, 803, 804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_801 import add_801
from module_802 import subtract_802
from module_803 import multiply_803
from module_804 import divide_804

def test_add_801():
    assert add_801(2, 3) == 5

def test_subtract_802():
    assert subtract_802(10, 4) == 6

def test_multiply_803():
    assert multiply_803(3, 7) == 21

def test_divide_804():
    assert divide_804(10, 2) == 5.0
