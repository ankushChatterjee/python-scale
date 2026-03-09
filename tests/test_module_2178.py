"""Tests for test module 2178 — covers src modules [8709, 8710, 8711, 8712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8709 import modulo_8709
from module_8710 import power_8710
from module_8711 import min_8711
from module_8712 import max_8712

def test_modulo_8709():
    assert modulo_8709(10, 3) == 1

def test_power_8710():
    assert power_8710(2, 8) == 256

def test_min_8711():
    assert min_8711(3, 7) == 3

def test_max_8712():
    assert max_8712(3, 7) == 7
