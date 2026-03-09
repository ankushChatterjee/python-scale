"""Tests for test module 1020 — covers src modules [4077, 4078, 4079, 4080]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4077 import modulo_4077
from module_4078 import power_4078
from module_4079 import min_4079
from module_4080 import max_4080

def test_modulo_4077():
    assert modulo_4077(10, 3) == 1

def test_power_4078():
    assert power_4078(2, 8) == 256

def test_min_4079():
    assert min_4079(3, 7) == 3

def test_max_4080():
    assert max_4080(3, 7) == 7
