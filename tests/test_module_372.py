"""Tests for test module 372 — covers src modules [1485, 1486, 1487, 1488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1485 import modulo_1485
from module_1486 import power_1486
from module_1487 import min_1487
from module_1488 import max_1488

def test_modulo_1485():
    assert modulo_1485(10, 3) == 1

def test_power_1486():
    assert power_1486(2, 8) == 256

def test_min_1487():
    assert min_1487(3, 7) == 3

def test_max_1488():
    assert max_1488(3, 7) == 7
