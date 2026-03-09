"""Tests for test module 634 — covers src modules [2533, 2534, 2535, 2536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2533 import modulo_2533
from module_2534 import power_2534
from module_2535 import min_2535
from module_2536 import max_2536

def test_modulo_2533():
    assert modulo_2533(10, 3) == 1

def test_power_2534():
    assert power_2534(2, 8) == 256

def test_min_2535():
    assert min_2535(3, 7) == 3

def test_max_2536():
    assert max_2536(3, 7) == 7
