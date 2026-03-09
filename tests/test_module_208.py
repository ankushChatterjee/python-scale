"""Tests for test module 208 — covers src modules [829, 830, 831, 832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_829 import modulo_829
from module_830 import power_830
from module_831 import min_831
from module_832 import max_832

def test_modulo_829():
    assert modulo_829(10, 3) == 1

def test_power_830():
    assert power_830(2, 8) == 256

def test_min_831():
    assert min_831(3, 7) == 3

def test_max_832():
    assert max_832(3, 7) == 7
