"""Tests for test module 2006 — covers src modules [8021, 8022, 8023, 8024]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8021 import modulo_8021
from module_8022 import power_8022
from module_8023 import min_8023
from module_8024 import max_8024

def test_modulo_8021():
    assert modulo_8021(10, 3) == 1

def test_power_8022():
    assert power_8022(2, 8) == 256

def test_min_8023():
    assert min_8023(3, 7) == 3

def test_max_8024():
    assert max_8024(3, 7) == 7
