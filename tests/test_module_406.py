"""Tests for test module 406 — covers src modules [1621, 1622, 1623, 1624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1621 import modulo_1621
from module_1622 import power_1622
from module_1623 import min_1623
from module_1624 import max_1624

def test_modulo_1621():
    assert modulo_1621(10, 3) == 1

def test_power_1622():
    assert power_1622(2, 8) == 256

def test_min_1623():
    assert min_1623(3, 7) == 3

def test_max_1624():
    assert max_1624(3, 7) == 7
