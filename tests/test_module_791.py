"""Tests for test module 791 — covers src modules [3161, 3162, 3163, 3164]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3161 import add_3161
from module_3162 import subtract_3162
from module_3163 import multiply_3163
from module_3164 import divide_3164

def test_add_3161():
    assert add_3161(2, 3) == 5

def test_subtract_3162():
    assert subtract_3162(10, 4) == 6

def test_multiply_3163():
    assert multiply_3163(3, 7) == 21

def test_divide_3164():
    assert divide_3164(10, 2) == 5.0
