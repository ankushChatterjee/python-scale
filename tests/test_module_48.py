"""Tests for test module 48 — covers src modules [189, 190, 191, 192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_189 import modulo_189
from module_190 import power_190
from module_191 import min_191
from module_192 import max_192

def test_modulo_189():
    assert modulo_189(10, 3) == 1

def test_power_190():
    assert power_190(2, 8) == 256

def test_min_191():
    assert min_191(3, 7) == 3

def test_max_192():
    assert max_192(3, 7) == 7
