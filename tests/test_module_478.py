"""Tests for test module 478 — covers src modules [1909, 1910, 1911, 1912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1909 import modulo_1909
from module_1910 import power_1910
from module_1911 import min_1911
from module_1912 import max_1912

def test_modulo_1909():
    assert modulo_1909(10, 3) == 1

def test_power_1910():
    assert power_1910(2, 8) == 256

def test_min_1911():
    assert min_1911(3, 7) == 3

def test_max_1912():
    assert max_1912(3, 7) == 7
