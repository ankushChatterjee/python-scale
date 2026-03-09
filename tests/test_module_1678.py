"""Tests for test module 1678 — covers src modules [6709, 6710, 6711, 6712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6709 import modulo_6709
from module_6710 import power_6710
from module_6711 import min_6711
from module_6712 import max_6712

def test_modulo_6709():
    assert modulo_6709(10, 3) == 1

def test_power_6710():
    assert power_6710(2, 8) == 256

def test_min_6711():
    assert min_6711(3, 7) == 3

def test_max_6712():
    assert max_6712(3, 7) == 7
