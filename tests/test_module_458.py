"""Tests for test module 458 — covers src modules [1829, 1830, 1831, 1832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1829 import modulo_1829
from module_1830 import power_1830
from module_1831 import min_1831
from module_1832 import max_1832

def test_modulo_1829():
    assert modulo_1829(10, 3) == 1

def test_power_1830():
    assert power_1830(2, 8) == 256

def test_min_1831():
    assert min_1831(3, 7) == 3

def test_max_1832():
    assert max_1832(3, 7) == 7
