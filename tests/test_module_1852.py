"""Tests for test module 1852 — covers src modules [7405, 7406, 7407, 7408]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7405 import modulo_7405
from module_7406 import power_7406
from module_7407 import min_7407
from module_7408 import max_7408

def test_modulo_7405():
    assert modulo_7405(10, 3) == 1

def test_power_7406():
    assert power_7406(2, 8) == 256

def test_min_7407():
    assert min_7407(3, 7) == 3

def test_max_7408():
    assert max_7408(3, 7) == 7
