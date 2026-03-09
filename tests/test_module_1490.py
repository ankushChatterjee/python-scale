"""Tests for test module 1490 — covers src modules [5957, 5958, 5959, 5960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5957 import modulo_5957
from module_5958 import power_5958
from module_5959 import min_5959
from module_5960 import max_5960

def test_modulo_5957():
    assert modulo_5957(10, 3) == 1

def test_power_5958():
    assert power_5958(2, 8) == 256

def test_min_5959():
    assert min_5959(3, 7) == 3

def test_max_5960():
    assert max_5960(3, 7) == 7
