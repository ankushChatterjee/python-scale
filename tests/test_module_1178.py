"""Tests for test module 1178 — covers src modules [4709, 4710, 4711, 4712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4709 import modulo_4709
from module_4710 import power_4710
from module_4711 import min_4711
from module_4712 import max_4712

def test_modulo_4709():
    assert modulo_4709(10, 3) == 1

def test_power_4710():
    assert power_4710(2, 8) == 256

def test_min_4711():
    assert min_4711(3, 7) == 3

def test_max_4712():
    assert max_4712(3, 7) == 7
