"""Tests for test module 1028 — covers src modules [4109, 4110, 4111, 4112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4109 import modulo_4109
from module_4110 import power_4110
from module_4111 import min_4111
from module_4112 import max_4112

def test_modulo_4109():
    assert modulo_4109(10, 3) == 1

def test_power_4110():
    assert power_4110(2, 8) == 256

def test_min_4111():
    assert min_4111(3, 7) == 3

def test_max_4112():
    assert max_4112(3, 7) == 7
