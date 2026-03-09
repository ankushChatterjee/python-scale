"""Tests for test module 1458 — covers src modules [5829, 5830, 5831, 5832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5829 import modulo_5829
from module_5830 import power_5830
from module_5831 import min_5831
from module_5832 import max_5832

def test_modulo_5829():
    assert modulo_5829(10, 3) == 1

def test_power_5830():
    assert power_5830(2, 8) == 256

def test_min_5831():
    assert min_5831(3, 7) == 3

def test_max_5832():
    assert max_5832(3, 7) == 7
