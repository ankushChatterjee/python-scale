"""Tests for test module 1174 — covers src modules [4693, 4694, 4695, 4696]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4693 import modulo_4693
from module_4694 import power_4694
from module_4695 import min_4695
from module_4696 import max_4696

def test_modulo_4693():
    assert modulo_4693(10, 3) == 1

def test_power_4694():
    assert power_4694(2, 8) == 256

def test_min_4695():
    assert min_4695(3, 7) == 3

def test_max_4696():
    assert max_4696(3, 7) == 7
