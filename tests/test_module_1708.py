"""Tests for test module 1708 — covers src modules [6829, 6830, 6831, 6832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6829 import modulo_6829
from module_6830 import power_6830
from module_6831 import min_6831
from module_6832 import max_6832

def test_modulo_6829():
    assert modulo_6829(10, 3) == 1

def test_power_6830():
    assert power_6830(2, 8) == 256

def test_min_6831():
    assert min_6831(3, 7) == 3

def test_max_6832():
    assert max_6832(3, 7) == 7
