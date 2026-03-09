"""Tests for test module 1520 — covers src modules [6077, 6078, 6079, 6080]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6077 import modulo_6077
from module_6078 import power_6078
from module_6079 import min_6079
from module_6080 import max_6080

def test_modulo_6077():
    assert modulo_6077(10, 3) == 1

def test_power_6078():
    assert power_6078(2, 8) == 256

def test_min_6079():
    assert min_6079(3, 7) == 3

def test_max_6080():
    assert max_6080(3, 7) == 7
