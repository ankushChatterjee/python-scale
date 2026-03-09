"""Tests for test module 1648 — covers src modules [6589, 6590, 6591, 6592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6589 import modulo_6589
from module_6590 import power_6590
from module_6591 import min_6591
from module_6592 import max_6592

def test_modulo_6589():
    assert modulo_6589(10, 3) == 1

def test_power_6590():
    assert power_6590(2, 8) == 256

def test_min_6591():
    assert min_6591(3, 7) == 3

def test_max_6592():
    assert max_6592(3, 7) == 7
