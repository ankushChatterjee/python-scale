"""Tests for test module 1636 — covers src modules [6541, 6542, 6543, 6544]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6541 import modulo_6541
from module_6542 import power_6542
from module_6543 import min_6543
from module_6544 import max_6544

def test_modulo_6541():
    assert modulo_6541(10, 3) == 1

def test_power_6542():
    assert power_6542(2, 8) == 256

def test_min_6543():
    assert min_6543(3, 7) == 3

def test_max_6544():
    assert max_6544(3, 7) == 7
