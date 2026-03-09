"""Tests for test module 1798 — covers src modules [7189, 7190, 7191, 7192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7189 import modulo_7189
from module_7190 import power_7190
from module_7191 import min_7191
from module_7192 import max_7192

def test_modulo_7189():
    assert modulo_7189(10, 3) == 1

def test_power_7190():
    assert power_7190(2, 8) == 256

def test_min_7191():
    assert min_7191(3, 7) == 3

def test_max_7192():
    assert max_7192(3, 7) == 7
