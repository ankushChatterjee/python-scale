"""Tests for test module 146 — covers src modules [581, 582, 583, 584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_581 import modulo_581
from module_582 import power_582
from module_583 import min_583
from module_584 import max_584

def test_modulo_581():
    assert modulo_581(10, 3) == 1

def test_power_582():
    assert power_582(2, 8) == 256

def test_min_583():
    assert min_583(3, 7) == 3

def test_max_584():
    assert max_584(3, 7) == 7
