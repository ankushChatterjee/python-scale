"""Tests for test module 1978 — covers src modules [7909, 7910, 7911, 7912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7909 import modulo_7909
from module_7910 import power_7910
from module_7911 import min_7911
from module_7912 import max_7912

def test_modulo_7909():
    assert modulo_7909(10, 3) == 1

def test_power_7910():
    assert power_7910(2, 8) == 256

def test_min_7911():
    assert min_7911(3, 7) == 3

def test_max_7912():
    assert max_7912(3, 7) == 7
