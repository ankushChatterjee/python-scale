"""Tests for test module 1390 — covers src modules [5557, 5558, 5559, 5560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5557 import modulo_5557
from module_5558 import power_5558
from module_5559 import min_5559
from module_5560 import max_5560

def test_modulo_5557():
    assert modulo_5557(10, 3) == 1

def test_power_5558():
    assert power_5558(2, 8) == 256

def test_min_5559():
    assert min_5559(3, 7) == 3

def test_max_5560():
    assert max_5560(3, 7) == 7
