"""Tests for test module 708 — covers src modules [2829, 2830, 2831, 2832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2829 import modulo_2829
from module_2830 import power_2830
from module_2831 import min_2831
from module_2832 import max_2832

def test_modulo_2829():
    assert modulo_2829(10, 3) == 1

def test_power_2830():
    assert power_2830(2, 8) == 256

def test_min_2831():
    assert min_2831(3, 7) == 3

def test_max_2832():
    assert max_2832(3, 7) == 7
