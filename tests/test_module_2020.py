"""Tests for test module 2020 — covers src modules [8077, 8078, 8079, 8080]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8077 import modulo_8077
from module_8078 import power_8078
from module_8079 import min_8079
from module_8080 import max_8080

def test_modulo_8077():
    assert modulo_8077(10, 3) == 1

def test_power_8078():
    assert power_8078(2, 8) == 256

def test_min_8079():
    assert min_8079(3, 7) == 3

def test_max_8080():
    assert max_8080(3, 7) == 7
