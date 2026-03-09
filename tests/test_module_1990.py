"""Tests for test module 1990 — covers src modules [7957, 7958, 7959, 7960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7957 import modulo_7957
from module_7958 import power_7958
from module_7959 import min_7959
from module_7960 import max_7960

def test_modulo_7957():
    assert modulo_7957(10, 3) == 1

def test_power_7958():
    assert power_7958(2, 8) == 256

def test_min_7959():
    assert min_7959(3, 7) == 3

def test_max_7960():
    assert max_7960(3, 7) == 7
