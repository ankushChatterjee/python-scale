"""Tests for test module 1756 — covers src modules [7021, 7022, 7023, 7024]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7021 import modulo_7021
from module_7022 import power_7022
from module_7023 import min_7023
from module_7024 import max_7024

def test_modulo_7021():
    assert modulo_7021(10, 3) == 1

def test_power_7022():
    assert power_7022(2, 8) == 256

def test_min_7023():
    assert min_7023(3, 7) == 3

def test_max_7024():
    assert max_7024(3, 7) == 7
