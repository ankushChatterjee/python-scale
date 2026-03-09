"""Tests for test module 2228 — covers src modules [8909, 8910, 8911, 8912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8909 import modulo_8909
from module_8910 import power_8910
from module_8911 import min_8911
from module_8912 import max_8912

def test_modulo_8909():
    assert modulo_8909(10, 3) == 1

def test_power_8910():
    assert power_8910(2, 8) == 256

def test_min_8911():
    assert min_8911(3, 7) == 3

def test_max_8912():
    assert max_8912(3, 7) == 7
