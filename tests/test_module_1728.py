"""Tests for test module 1728 — covers src modules [6909, 6910, 6911, 6912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6909 import modulo_6909
from module_6910 import power_6910
from module_6911 import min_6911
from module_6912 import max_6912

def test_modulo_6909():
    assert modulo_6909(10, 3) == 1

def test_power_6910():
    assert power_6910(2, 8) == 256

def test_min_6911():
    assert min_6911(3, 7) == 3

def test_max_6912():
    assert max_6912(3, 7) == 7
