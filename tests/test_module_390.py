"""Tests for test module 390 — covers src modules [1557, 1558, 1559, 1560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1557 import modulo_1557
from module_1558 import power_1558
from module_1559 import min_1559
from module_1560 import max_1560

def test_modulo_1557():
    assert modulo_1557(10, 3) == 1

def test_power_1558():
    assert power_1558(2, 8) == 256

def test_min_1559():
    assert min_1559(3, 7) == 3

def test_max_1560():
    assert max_1560(3, 7) == 7
