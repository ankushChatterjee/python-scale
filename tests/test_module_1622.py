"""Tests for test module 1622 — covers src modules [6485, 6486, 6487, 6488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6485 import modulo_6485
from module_6486 import power_6486
from module_6487 import min_6487
from module_6488 import max_6488

def test_modulo_6485():
    assert modulo_6485(10, 3) == 1

def test_power_6486():
    assert power_6486(2, 8) == 256

def test_min_6487():
    assert min_6487(3, 7) == 3

def test_max_6488():
    assert max_6488(3, 7) == 7
