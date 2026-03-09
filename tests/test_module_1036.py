"""Tests for test module 1036 — covers src modules [4141, 4142, 4143, 4144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4141 import modulo_4141
from module_4142 import power_4142
from module_4143 import min_4143
from module_4144 import max_4144

def test_modulo_4141():
    assert modulo_4141(10, 3) == 1

def test_power_4142():
    assert power_4142(2, 8) == 256

def test_min_4143():
    assert min_4143(3, 7) == 3

def test_max_4144():
    assert max_4144(3, 7) == 7
