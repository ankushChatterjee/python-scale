"""Tests for test module 240 — covers src modules [957, 958, 959, 960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_957 import modulo_957
from module_958 import power_958
from module_959 import min_959
from module_960 import max_960

def test_modulo_957():
    assert modulo_957(10, 3) == 1

def test_power_958():
    assert power_958(2, 8) == 256

def test_min_959():
    assert min_959(3, 7) == 3

def test_max_960():
    assert max_960(3, 7) == 7
