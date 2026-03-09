"""Tests for test module 1640 — covers src modules [6557, 6558, 6559, 6560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6557 import modulo_6557
from module_6558 import power_6558
from module_6559 import min_6559
from module_6560 import max_6560

def test_modulo_6557():
    assert modulo_6557(10, 3) == 1

def test_power_6558():
    assert power_6558(2, 8) == 256

def test_min_6559():
    assert min_6559(3, 7) == 3

def test_max_6560():
    assert max_6560(3, 7) == 7
