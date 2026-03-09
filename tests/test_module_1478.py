"""Tests for test module 1478 — covers src modules [5909, 5910, 5911, 5912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5909 import modulo_5909
from module_5910 import power_5910
from module_5911 import min_5911
from module_5912 import max_5912

def test_modulo_5909():
    assert modulo_5909(10, 3) == 1

def test_power_5910():
    assert power_5910(2, 8) == 256

def test_min_5911():
    assert min_5911(3, 7) == 3

def test_max_5912():
    assert max_5912(3, 7) == 7
