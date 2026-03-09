"""Tests for test module 508 — covers src modules [2029, 2030, 2031, 2032]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2029 import modulo_2029
from module_2030 import power_2030
from module_2031 import min_2031
from module_2032 import max_2032

def test_modulo_2029():
    assert modulo_2029(10, 3) == 1

def test_power_2030():
    assert power_2030(2, 8) == 256

def test_min_2031():
    assert min_2031(3, 7) == 3

def test_max_2032():
    assert max_2032(3, 7) == 7
