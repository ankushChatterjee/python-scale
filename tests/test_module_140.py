"""Tests for test module 140 — covers src modules [557, 558, 559, 560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_557 import modulo_557
from module_558 import power_558
from module_559 import min_559
from module_560 import max_560

def test_modulo_557():
    assert modulo_557(10, 3) == 1

def test_power_558():
    assert power_558(2, 8) == 256

def test_min_559():
    assert min_559(3, 7) == 3

def test_max_560():
    assert max_560(3, 7) == 7
