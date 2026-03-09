"""Tests for test module 102 — covers src modules [405, 406, 407, 408]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_405 import modulo_405
from module_406 import power_406
from module_407 import min_407
from module_408 import max_408

def test_modulo_405():
    assert modulo_405(10, 3) == 1

def test_power_406():
    assert power_406(2, 8) == 256

def test_min_407():
    assert min_407(3, 7) == 3

def test_max_408():
    assert max_408(3, 7) == 7
