"""Tests for test module 1006 — covers src modules [4021, 4022, 4023, 4024]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4021 import modulo_4021
from module_4022 import power_4022
from module_4023 import min_4023
from module_4024 import max_4024

def test_modulo_4021():
    assert modulo_4021(10, 3) == 1

def test_power_4022():
    assert power_4022(2, 8) == 256

def test_min_4023():
    assert min_4023(3, 7) == 3

def test_max_4024():
    assert max_4024(3, 7) == 7
