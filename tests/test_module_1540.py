"""Tests for test module 1540 — covers src modules [6157, 6158, 6159, 6160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6157 import modulo_6157
from module_6158 import power_6158
from module_6159 import min_6159
from module_6160 import max_6160

def test_modulo_6157():
    assert modulo_6157(10, 3) == 1

def test_power_6158():
    assert power_6158(2, 8) == 256

def test_min_6159():
    assert min_6159(3, 7) == 3

def test_max_6160():
    assert max_6160(3, 7) == 7
