"""Tests for test module 1898 — covers src modules [7589, 7590, 7591, 7592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7589 import modulo_7589
from module_7590 import power_7590
from module_7591 import min_7591
from module_7592 import max_7592

def test_modulo_7589():
    assert modulo_7589(10, 3) == 1

def test_power_7590():
    assert power_7590(2, 8) == 256

def test_min_7591():
    assert min_7591(3, 7) == 3

def test_max_7592():
    assert max_7592(3, 7) == 7
