"""Tests for test module 1896 — covers src modules [7581, 7582, 7583, 7584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7581 import modulo_7581
from module_7582 import power_7582
from module_7583 import min_7583
from module_7584 import max_7584

def test_modulo_7581():
    assert modulo_7581(10, 3) == 1

def test_power_7582():
    assert power_7582(2, 8) == 256

def test_min_7583():
    assert min_7583(3, 7) == 3

def test_max_7584():
    assert max_7584(3, 7) == 7
