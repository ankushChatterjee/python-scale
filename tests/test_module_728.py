"""Tests for test module 728 — covers src modules [2909, 2910, 2911, 2912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2909 import modulo_2909
from module_2910 import power_2910
from module_2911 import min_2911
from module_2912 import max_2912

def test_modulo_2909():
    assert modulo_2909(10, 3) == 1

def test_power_2910():
    assert power_2910(2, 8) == 256

def test_min_2911():
    assert min_2911(3, 7) == 3

def test_max_2912():
    assert max_2912(3, 7) == 7
