"""Tests for test module 606 — covers src modules [2421, 2422, 2423, 2424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2421 import modulo_2421
from module_2422 import power_2422
from module_2423 import min_2423
from module_2424 import max_2424

def test_modulo_2421():
    assert modulo_2421(10, 3) == 1

def test_power_2422():
    assert power_2422(2, 8) == 256

def test_min_2423():
    assert min_2423(3, 7) == 3

def test_max_2424():
    assert max_2424(3, 7) == 7
