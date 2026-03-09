"""Tests for test module 148 — covers src modules [589, 590, 591, 592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_589 import modulo_589
from module_590 import power_590
from module_591 import min_591
from module_592 import max_592

def test_modulo_589():
    assert modulo_589(10, 3) == 1

def test_power_590():
    assert power_590(2, 8) == 256

def test_min_591():
    assert min_591(3, 7) == 3

def test_max_592():
    assert max_592(3, 7) == 7
