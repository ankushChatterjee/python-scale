"""Tests for test module 2041 — covers src modules [8161, 8162, 8163, 8164]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8161 import add_8161
from module_8162 import subtract_8162
from module_8163 import multiply_8163
from module_8164 import divide_8164

def test_add_8161():
    assert add_8161(2, 3) == 5

def test_subtract_8162():
    assert subtract_8162(10, 4) == 6

def test_multiply_8163():
    assert multiply_8163(3, 7) == 21

def test_divide_8164():
    assert divide_8164(10, 2) == 5.0
