"""Tests for test module 2208 — covers src modules [8829, 8830, 8831, 8832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8829 import modulo_8829
from module_8830 import power_8830
from module_8831 import min_8831
from module_8832 import max_8832

def test_modulo_8829():
    assert modulo_8829(10, 3) == 1

def test_power_8830():
    assert power_8830(2, 8) == 256

def test_min_8831():
    assert min_8831(3, 7) == 3

def test_max_8832():
    assert max_8832(3, 7) == 7
