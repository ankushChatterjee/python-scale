"""Tests for test module 898 — covers src modules [3589, 3590, 3591, 3592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3589 import modulo_3589
from module_3590 import power_3590
from module_3591 import min_3591
from module_3592 import max_3592

def test_modulo_3589():
    assert modulo_3589(10, 3) == 1

def test_power_3590():
    assert power_3590(2, 8) == 256

def test_min_3591():
    assert min_3591(3, 7) == 3

def test_max_3592():
    assert max_3592(3, 7) == 7
