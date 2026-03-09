"""Tests for test module 1646 — covers src modules [6581, 6582, 6583, 6584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6581 import modulo_6581
from module_6582 import power_6582
from module_6583 import min_6583
from module_6584 import max_6584

def test_modulo_6581():
    assert modulo_6581(10, 3) == 1

def test_power_6582():
    assert power_6582(2, 8) == 256

def test_min_6583():
    assert min_6583(3, 7) == 3

def test_max_6584():
    assert max_6584(3, 7) == 7
