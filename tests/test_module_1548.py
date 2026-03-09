"""Tests for test module 1548 — covers src modules [6189, 6190, 6191, 6192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6189 import modulo_6189
from module_6190 import power_6190
from module_6191 import min_6191
from module_6192 import max_6192

def test_modulo_6189():
    assert modulo_6189(10, 3) == 1

def test_power_6190():
    assert power_6190(2, 8) == 256

def test_min_6191():
    assert min_6191(3, 7) == 3

def test_max_6192():
    assert max_6192(3, 7) == 7
