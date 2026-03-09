"""Tests for test module 490 — covers src modules [1957, 1958, 1959, 1960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1957 import modulo_1957
from module_1958 import power_1958
from module_1959 import min_1959
from module_1960 import max_1960

def test_modulo_1957():
    assert modulo_1957(10, 3) == 1

def test_power_1958():
    assert power_1958(2, 8) == 256

def test_min_1959():
    assert min_1959(3, 7) == 3

def test_max_1960():
    assert max_1960(3, 7) == 7
