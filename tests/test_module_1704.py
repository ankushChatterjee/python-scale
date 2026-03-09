"""Tests for test module 1704 — covers src modules [6813, 6814, 6815, 6816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6813 import modulo_6813
from module_6814 import power_6814
from module_6815 import min_6815
from module_6816 import max_6816

def test_modulo_6813():
    assert modulo_6813(10, 3) == 1

def test_power_6814():
    assert power_6814(2, 8) == 256

def test_min_6815():
    assert min_6815(3, 7) == 3

def test_max_6816():
    assert max_6816(3, 7) == 7
