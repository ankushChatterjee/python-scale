"""Tests for test module 740 — covers src modules [2957, 2958, 2959, 2960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2957 import modulo_2957
from module_2958 import power_2958
from module_2959 import min_2959
from module_2960 import max_2960

def test_modulo_2957():
    assert modulo_2957(10, 3) == 1

def test_power_2958():
    assert power_2958(2, 8) == 256

def test_min_2959():
    assert min_2959(3, 7) == 3

def test_max_2960():
    assert max_2960(3, 7) == 7
