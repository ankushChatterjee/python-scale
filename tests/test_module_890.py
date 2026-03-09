"""Tests for test module 890 — covers src modules [3557, 3558, 3559, 3560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3557 import modulo_3557
from module_3558 import power_3558
from module_3559 import min_3559
from module_3560 import max_3560

def test_modulo_3557():
    assert modulo_3557(10, 3) == 1

def test_power_3558():
    assert power_3558(2, 8) == 256

def test_min_3559():
    assert min_3559(3, 7) == 3

def test_max_3560():
    assert max_3560(3, 7) == 7
