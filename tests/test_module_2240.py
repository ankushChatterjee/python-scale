"""Tests for test module 2240 — covers src modules [8957, 8958, 8959, 8960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8957 import modulo_8957
from module_8958 import power_8958
from module_8959 import min_8959
from module_8960 import max_8960

def test_modulo_8957():
    assert modulo_8957(10, 3) == 1

def test_power_8958():
    assert power_8958(2, 8) == 256

def test_min_8959():
    assert min_8959(3, 7) == 3

def test_max_8960():
    assert max_8960(3, 7) == 7
