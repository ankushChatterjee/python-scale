"""Tests for test module 2148 — covers src modules [8589, 8590, 8591, 8592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8589 import modulo_8589
from module_8590 import power_8590
from module_8591 import min_8591
from module_8592 import max_8592

def test_modulo_8589():
    assert modulo_8589(10, 3) == 1

def test_power_8590():
    assert power_8590(2, 8) == 256

def test_min_8591():
    assert min_8591(3, 7) == 3

def test_max_8592():
    assert max_8592(3, 7) == 7
