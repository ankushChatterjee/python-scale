"""Tests for test module 228 — covers src modules [909, 910, 911, 912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_909 import modulo_909
from module_910 import power_910
from module_911 import min_911
from module_912 import max_912

def test_modulo_909():
    assert modulo_909(10, 3) == 1

def test_power_910():
    assert power_910(2, 8) == 256

def test_min_911():
    assert min_911(3, 7) == 3

def test_max_912():
    assert max_912(3, 7) == 7
