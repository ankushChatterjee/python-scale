"""Tests for test module 2245 — covers src modules [8977, 8978, 8979, 8980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8977 import add_8977
from module_8978 import subtract_8978
from module_8979 import multiply_8979
from module_8980 import divide_8980

def test_add_8977():
    assert add_8977(2, 3) == 5

def test_subtract_8978():
    assert subtract_8978(10, 4) == 6

def test_multiply_8979():
    assert multiply_8979(3, 7) == 21

def test_divide_8980():
    assert divide_8980(10, 2) == 5.0
