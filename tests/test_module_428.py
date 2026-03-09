"""Tests for test module 428 — covers src modules [1709, 1710, 1711, 1712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1709 import modulo_1709
from module_1710 import power_1710
from module_1711 import min_1711
from module_1712 import max_1712

def test_modulo_1709():
    assert modulo_1709(10, 3) == 1

def test_power_1710():
    assert power_1710(2, 8) == 256

def test_min_1711():
    assert min_1711(3, 7) == 3

def test_max_1712():
    assert max_1712(3, 7) == 7
