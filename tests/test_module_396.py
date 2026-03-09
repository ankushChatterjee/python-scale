"""Tests for test module 396 — covers src modules [1581, 1582, 1583, 1584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1581 import modulo_1581
from module_1582 import power_1582
from module_1583 import min_1583
from module_1584 import max_1584

def test_modulo_1581():
    assert modulo_1581(10, 3) == 1

def test_power_1582():
    assert power_1582(2, 8) == 256

def test_min_1583():
    assert min_1583(3, 7) == 3

def test_max_1584():
    assert max_1584(3, 7) == 7
