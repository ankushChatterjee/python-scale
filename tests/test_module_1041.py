"""Tests for test module 1041 — covers src modules [4161, 4162, 4163, 4164]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4161 import add_4161
from module_4162 import subtract_4162
from module_4163 import multiply_4163
from module_4164 import divide_4164

def test_add_4161():
    assert add_4161(2, 3) == 5

def test_subtract_4162():
    assert subtract_4162(10, 4) == 6

def test_multiply_4163():
    assert multiply_4163(3, 7) == 21

def test_divide_4164():
    assert divide_4164(10, 2) == 5.0
