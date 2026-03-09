"""Tests for test module 644 — covers src modules [2573, 2574, 2575, 2576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2573 import modulo_2573
from module_2574 import power_2574
from module_2575 import min_2575
from module_2576 import max_2576

def test_modulo_2573():
    assert modulo_2573(10, 3) == 1

def test_power_2574():
    assert power_2574(2, 8) == 256

def test_min_2575():
    assert min_2575(3, 7) == 3

def test_max_2576():
    assert max_2576(3, 7) == 7
