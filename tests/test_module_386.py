"""Tests for test module 386 — covers src modules [1541, 1542, 1543, 1544]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1541 import modulo_1541
from module_1542 import power_1542
from module_1543 import min_1543
from module_1544 import max_1544

def test_modulo_1541():
    assert modulo_1541(10, 3) == 1

def test_power_1542():
    assert power_1542(2, 8) == 256

def test_min_1543():
    assert min_1543(3, 7) == 3

def test_max_1544():
    assert max_1544(3, 7) == 7
