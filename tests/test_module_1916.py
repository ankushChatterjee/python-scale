"""Tests for test module 1916 — covers src modules [7661, 7662, 7663, 7664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7661 import modulo_7661
from module_7662 import power_7662
from module_7663 import min_7663
from module_7664 import max_7664

def test_modulo_7661():
    assert modulo_7661(10, 3) == 1

def test_power_7662():
    assert power_7662(2, 8) == 256

def test_min_7663():
    assert min_7663(3, 7) == 3

def test_max_7664():
    assert max_7664(3, 7) == 7
