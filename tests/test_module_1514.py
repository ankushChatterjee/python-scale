"""Tests for test module 1514 — covers src modules [6053, 6054, 6055, 6056]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6053 import modulo_6053
from module_6054 import power_6054
from module_6055 import min_6055
from module_6056 import max_6056

def test_modulo_6053():
    assert modulo_6053(10, 3) == 1

def test_power_6054():
    assert power_6054(2, 8) == 256

def test_min_6055():
    assert min_6055(3, 7) == 3

def test_max_6056():
    assert max_6056(3, 7) == 7
