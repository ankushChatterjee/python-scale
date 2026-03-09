"""Tests for test module 1890 — covers src modules [7557, 7558, 7559, 7560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7557 import modulo_7557
from module_7558 import power_7558
from module_7559 import min_7559
from module_7560 import max_7560

def test_modulo_7557():
    assert modulo_7557(10, 3) == 1

def test_power_7558():
    assert power_7558(2, 8) == 256

def test_min_7559():
    assert min_7559(3, 7) == 3

def test_max_7560():
    assert max_7560(3, 7) == 7
