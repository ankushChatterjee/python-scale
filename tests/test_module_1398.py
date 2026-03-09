"""Tests for test module 1398 — covers src modules [5589, 5590, 5591, 5592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5589 import modulo_5589
from module_5590 import power_5590
from module_5591 import min_5591
from module_5592 import max_5592

def test_modulo_5589():
    assert modulo_5589(10, 3) == 1

def test_power_5590():
    assert power_5590(2, 8) == 256

def test_min_5591():
    assert min_5591(3, 7) == 3

def test_max_5592():
    assert max_5592(3, 7) == 7
