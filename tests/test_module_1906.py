"""Tests for test module 1906 — covers src modules [7621, 7622, 7623, 7624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7621 import modulo_7621
from module_7622 import power_7622
from module_7623 import min_7623
from module_7624 import max_7624

def test_modulo_7621():
    assert modulo_7621(10, 3) == 1

def test_power_7622():
    assert power_7622(2, 8) == 256

def test_min_7623():
    assert min_7623(3, 7) == 3

def test_max_7624():
    assert max_7624(3, 7) == 7
