"""Tests for test module 1886 — covers src modules [7541, 7542, 7543, 7544]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7541 import modulo_7541
from module_7542 import power_7542
from module_7543 import min_7543
from module_7544 import max_7544

def test_modulo_7541():
    assert modulo_7541(10, 3) == 1

def test_power_7542():
    assert power_7542(2, 8) == 256

def test_min_7543():
    assert min_7543(3, 7) == 3

def test_max_7544():
    assert max_7544(3, 7) == 7
