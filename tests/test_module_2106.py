"""Tests for test module 2106 — covers src modules [8421, 8422, 8423, 8424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8421 import modulo_8421
from module_8422 import power_8422
from module_8423 import min_8423
from module_8424 import max_8424

def test_modulo_8421():
    assert modulo_8421(10, 3) == 1

def test_power_8422():
    assert power_8422(2, 8) == 256

def test_min_8423():
    assert min_8423(3, 7) == 3

def test_max_8424():
    assert max_8424(3, 7) == 7
