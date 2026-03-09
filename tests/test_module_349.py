"""Tests for test module 349 — covers src modules [1393, 1394, 1395, 1396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1393 import add_1393
from module_1394 import subtract_1394
from module_1395 import multiply_1395
from module_1396 import divide_1396

def test_add_1393():
    assert add_1393(2, 3) == 5

def test_subtract_1394():
    assert subtract_1394(10, 4) == 6

def test_multiply_1395():
    assert multiply_1395(3, 7) == 21

def test_divide_1396():
    assert divide_1396(10, 2) == 5.0
