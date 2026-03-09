"""Tests for test module 656 — covers src modules [2621, 2622, 2623, 2624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2621 import modulo_2621
from module_2622 import power_2622
from module_2623 import min_2623
from module_2624 import max_2624

def test_modulo_2621():
    assert modulo_2621(10, 3) == 1

def test_power_2622():
    assert power_2622(2, 8) == 256

def test_min_2623():
    assert min_2623(3, 7) == 3

def test_max_2624():
    assert max_2624(3, 7) == 7
