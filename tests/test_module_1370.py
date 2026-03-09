"""Tests for test module 1370 — covers src modules [5477, 5478, 5479, 5480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5477 import modulo_5477
from module_5478 import power_5478
from module_5479 import min_5479
from module_5480 import max_5480

def test_modulo_5477():
    assert modulo_5477(10, 3) == 1

def test_power_5478():
    assert power_5478(2, 8) == 256

def test_min_5479():
    assert min_5479(3, 7) == 3

def test_max_5480():
    assert max_5480(3, 7) == 7
