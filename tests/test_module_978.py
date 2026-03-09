"""Tests for test module 978 — covers src modules [3909, 3910, 3911, 3912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3909 import modulo_3909
from module_3910 import power_3910
from module_3911 import min_3911
from module_3912 import max_3912

def test_modulo_3909():
    assert modulo_3909(10, 3) == 1

def test_power_3910():
    assert power_3910(2, 8) == 256

def test_min_3911():
    assert min_3911(3, 7) == 3

def test_max_3912():
    assert max_3912(3, 7) == 7
