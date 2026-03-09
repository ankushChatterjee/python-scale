"""Tests for test module 2102 — covers src modules [8405, 8406, 8407, 8408]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8405 import modulo_8405
from module_8406 import power_8406
from module_8407 import min_8407
from module_8408 import max_8408

def test_modulo_8405():
    assert modulo_8405(10, 3) == 1

def test_power_8406():
    assert power_8406(2, 8) == 256

def test_min_8407():
    assert min_8407(3, 7) == 3

def test_max_8408():
    assert max_8408(3, 7) == 7
