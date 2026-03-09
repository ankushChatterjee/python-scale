"""Tests for test module 1228 — covers src modules [4909, 4910, 4911, 4912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4909 import modulo_4909
from module_4910 import power_4910
from module_4911 import min_4911
from module_4912 import max_4912

def test_modulo_4909():
    assert modulo_4909(10, 3) == 1

def test_power_4910():
    assert power_4910(2, 8) == 256

def test_min_4911():
    assert min_4911(3, 7) == 3

def test_max_4912():
    assert max_4912(3, 7) == 7
