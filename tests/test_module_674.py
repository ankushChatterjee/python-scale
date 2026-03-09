"""Tests for test module 674 — covers src modules [2693, 2694, 2695, 2696]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2693 import modulo_2693
from module_2694 import power_2694
from module_2695 import min_2695
from module_2696 import max_2696

def test_modulo_2693():
    assert modulo_2693(10, 3) == 1

def test_power_2694():
    assert power_2694(2, 8) == 256

def test_min_2695():
    assert min_2695(3, 7) == 3

def test_max_2696():
    assert max_2696(3, 7) == 7
