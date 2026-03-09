"""Tests for test module 1042 — covers src modules [4165, 4166, 4167, 4168]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4165 import modulo_4165
from module_4166 import power_4166
from module_4167 import min_4167
from module_4168 import max_4168

def test_modulo_4165():
    assert modulo_4165(10, 3) == 1

def test_power_4166():
    assert power_4166(2, 8) == 256

def test_min_4167():
    assert min_4167(3, 7) == 3

def test_max_4168():
    assert max_4168(3, 7) == 7
