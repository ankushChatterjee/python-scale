"""Tests for test module 1542 — covers src modules [6165, 6166, 6167, 6168]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6165 import modulo_6165
from module_6166 import power_6166
from module_6167 import min_6167
from module_6168 import max_6168

def test_modulo_6165():
    assert modulo_6165(10, 3) == 1

def test_power_6166():
    assert power_6166(2, 8) == 256

def test_min_6167():
    assert min_6167(3, 7) == 3

def test_max_6168():
    assert max_6168(3, 7) == 7
