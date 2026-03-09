"""Tests for test module 1849 — covers src modules [7393, 7394, 7395, 7396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7393 import add_7393
from module_7394 import subtract_7394
from module_7395 import multiply_7395
from module_7396 import divide_7396

def test_add_7393():
    assert add_7393(2, 3) == 5

def test_subtract_7394():
    assert subtract_7394(10, 4) == 6

def test_multiply_7395():
    assert multiply_7395(3, 7) == 21

def test_divide_7396():
    assert divide_7396(10, 2) == 5.0
