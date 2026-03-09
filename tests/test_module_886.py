"""Tests for test module 886 — covers src modules [3541, 3542, 3543, 3544]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3541 import modulo_3541
from module_3542 import power_3542
from module_3543 import min_3543
from module_3544 import max_3544

def test_modulo_3541():
    assert modulo_3541(10, 3) == 1

def test_power_3542():
    assert power_3542(2, 8) == 256

def test_min_3543():
    assert min_3543(3, 7) == 3

def test_max_3544():
    assert max_3544(3, 7) == 7
