"""Tests for test module 648 — covers src modules [2589, 2590, 2591, 2592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2589 import modulo_2589
from module_2590 import power_2590
from module_2591 import min_2591
from module_2592 import max_2592

def test_modulo_2589():
    assert modulo_2589(10, 3) == 1

def test_power_2590():
    assert power_2590(2, 8) == 256

def test_min_2591():
    assert min_2591(3, 7) == 3

def test_max_2592():
    assert max_2592(3, 7) == 7
