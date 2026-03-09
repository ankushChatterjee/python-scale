"""Tests for test module 640 — covers src modules [2557, 2558, 2559, 2560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2557 import modulo_2557
from module_2558 import power_2558
from module_2559 import min_2559
from module_2560 import max_2560

def test_modulo_2557():
    assert modulo_2557(10, 3) == 1

def test_power_2558():
    assert power_2558(2, 8) == 256

def test_min_2559():
    assert min_2559(3, 7) == 3

def test_max_2560():
    assert max_2560(3, 7) == 7
