"""Tests for test module 1396 — covers src modules [5581, 5582, 5583, 5584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5581 import modulo_5581
from module_5582 import power_5582
from module_5583 import min_5583
from module_5584 import max_5584

def test_modulo_5581():
    assert modulo_5581(10, 3) == 1

def test_power_5582():
    assert power_5582(2, 8) == 256

def test_min_5583():
    assert min_5583(3, 7) == 3

def test_max_5584():
    assert max_5584(3, 7) == 7
