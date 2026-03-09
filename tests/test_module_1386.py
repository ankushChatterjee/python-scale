"""Tests for test module 1386 — covers src modules [5541, 5542, 5543, 5544]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5541 import modulo_5541
from module_5542 import power_5542
from module_5543 import min_5543
from module_5544 import max_5544

def test_modulo_5541():
    assert modulo_5541(10, 3) == 1

def test_power_5542():
    assert power_5542(2, 8) == 256

def test_min_5543():
    assert min_5543(3, 7) == 3

def test_max_5544():
    assert max_5544(3, 7) == 7
