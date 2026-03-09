"""Tests for test module 1674 — covers src modules [6693, 6694, 6695, 6696]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6693 import modulo_6693
from module_6694 import power_6694
from module_6695 import min_6695
from module_6696 import max_6696

def test_modulo_6693():
    assert modulo_6693(10, 3) == 1

def test_power_6694():
    assert power_6694(2, 8) == 256

def test_min_6695():
    assert min_6695(3, 7) == 3

def test_max_6696():
    assert max_6696(3, 7) == 7
