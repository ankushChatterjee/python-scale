"""Tests for test module 844 — covers src modules [3373, 3374, 3375, 3376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3373 import modulo_3373
from module_3374 import power_3374
from module_3375 import min_3375
from module_3376 import max_3376

def test_modulo_3373():
    assert modulo_3373(10, 3) == 1

def test_power_3374():
    assert power_3374(2, 8) == 256

def test_min_3375():
    assert min_3375(3, 7) == 3

def test_max_3376():
    assert max_3376(3, 7) == 7
