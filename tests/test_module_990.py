"""Tests for test module 990 — covers src modules [3957, 3958, 3959, 3960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3957 import modulo_3957
from module_3958 import power_3958
from module_3959 import min_3959
from module_3960 import max_3960

def test_modulo_3957():
    assert modulo_3957(10, 3) == 1

def test_power_3958():
    assert power_3958(2, 8) == 256

def test_min_3959():
    assert min_3959(3, 7) == 3

def test_max_3960():
    assert max_3960(3, 7) == 7
