"""Tests for test module 636 — covers src modules [2541, 2542, 2543, 2544]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2541 import modulo_2541
from module_2542 import power_2542
from module_2543 import min_2543
from module_2544 import max_2544

def test_modulo_2541():
    assert modulo_2541(10, 3) == 1

def test_power_2542():
    assert power_2542(2, 8) == 256

def test_min_2543():
    assert min_2543(3, 7) == 3

def test_max_2544():
    assert max_2544(3, 7) == 7
