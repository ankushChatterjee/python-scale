"""Tests for test module 466 — covers src modules [1861, 1862, 1863, 1864]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1861 import modulo_1861
from module_1862 import power_1862
from module_1863 import min_1863
from module_1864 import max_1864

def test_modulo_1861():
    assert modulo_1861(10, 3) == 1

def test_power_1862():
    assert power_1862(2, 8) == 256

def test_min_1863():
    assert min_1863(3, 7) == 3

def test_max_1864():
    assert max_1864(3, 7) == 7
