"""Tests for test module 398 — covers src modules [1589, 1590, 1591, 1592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1589 import modulo_1589
from module_1590 import power_1590
from module_1591 import min_1591
from module_1592 import max_1592

def test_modulo_1589():
    assert modulo_1589(10, 3) == 1

def test_power_1590():
    assert power_1590(2, 8) == 256

def test_min_1591():
    assert min_1591(3, 7) == 3

def test_max_1592():
    assert max_1592(3, 7) == 7
