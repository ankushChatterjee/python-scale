"""Tests for test module 924 — covers src modules [3693, 3694, 3695, 3696]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3693 import modulo_3693
from module_3694 import power_3694
from module_3695 import min_3695
from module_3696 import max_3696

def test_modulo_3693():
    assert modulo_3693(10, 3) == 1

def test_power_3694():
    assert power_3694(2, 8) == 256

def test_min_3695():
    assert min_3695(3, 7) == 3

def test_max_3696():
    assert max_3696(3, 7) == 7
