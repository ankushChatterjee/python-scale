"""Tests for test module 370 — covers src modules [1477, 1478, 1479, 1480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1477 import modulo_1477
from module_1478 import power_1478
from module_1479 import min_1479
from module_1480 import max_1480

def test_modulo_1477():
    assert modulo_1477(10, 3) == 1

def test_power_1478():
    assert power_1478(2, 8) == 256

def test_min_1479():
    assert min_1479(3, 7) == 3

def test_max_1480():
    assert max_1480(3, 7) == 7
