"""Tests for test module 1356 — covers src modules [5421, 5422, 5423, 5424]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5421 import modulo_5421
from module_5422 import power_5422
from module_5423 import min_5423
from module_5424 import max_5424

def test_modulo_5421():
    assert modulo_5421(10, 3) == 1

def test_power_5422():
    assert power_5422(2, 8) == 256

def test_min_5423():
    assert min_5423(3, 7) == 3

def test_max_5424():
    assert max_5424(3, 7) == 7
