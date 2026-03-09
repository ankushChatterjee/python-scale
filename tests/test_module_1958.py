"""Tests for test module 1958 — covers src modules [7829, 7830, 7831, 7832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7829 import modulo_7829
from module_7830 import power_7830
from module_7831 import min_7831
from module_7832 import max_7832

def test_modulo_7829():
    assert modulo_7829(10, 3) == 1

def test_power_7830():
    assert power_7830(2, 8) == 256

def test_min_7831():
    assert min_7831(3, 7) == 3

def test_max_7832():
    assert max_7832(3, 7) == 7
