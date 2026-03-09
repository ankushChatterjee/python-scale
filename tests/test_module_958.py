"""Tests for test module 958 — covers src modules [3829, 3830, 3831, 3832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3829 import modulo_3829
from module_3830 import power_3830
from module_3831 import min_3831
from module_3832 import max_3832

def test_modulo_3829():
    assert modulo_3829(10, 3) == 1

def test_power_3830():
    assert power_3830(2, 8) == 256

def test_min_3831():
    assert min_3831(3, 7) == 3

def test_max_3832():
    assert max_3832(3, 7) == 7
