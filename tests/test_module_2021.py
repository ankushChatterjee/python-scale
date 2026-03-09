"""Tests for test module 2021 — covers src modules [8081, 8082, 8083, 8084]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8081 import add_8081
from module_8082 import subtract_8082
from module_8083 import multiply_8083
from module_8084 import divide_8084

def test_add_8081():
    assert add_8081(2, 3) == 5

def test_subtract_8082():
    assert subtract_8082(10, 4) == 6

def test_multiply_8083():
    assert multiply_8083(3, 7) == 21

def test_divide_8084():
    assert divide_8084(10, 2) == 5.0
