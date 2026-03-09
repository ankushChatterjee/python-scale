"""Tests for test module 896 — covers src modules [3581, 3582, 3583, 3584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3581 import modulo_3581
from module_3582 import power_3582
from module_3583 import min_3583
from module_3584 import max_3584

def test_modulo_3581():
    assert modulo_3581(10, 3) == 1

def test_power_3582():
    assert power_3582(2, 8) == 256

def test_min_3583():
    assert min_3583(3, 7) == 3

def test_max_3584():
    assert max_3584(3, 7) == 7
