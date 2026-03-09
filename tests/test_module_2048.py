"""Tests for test module 2048 — covers src modules [8189, 8190, 8191, 8192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8189 import modulo_8189
from module_8190 import power_8190
from module_8191 import min_8191
from module_8192 import max_8192

def test_modulo_8189():
    assert modulo_8189(10, 3) == 1

def test_power_8190():
    assert power_8190(2, 8) == 256

def test_min_8191():
    assert min_8191(3, 7) == 3

def test_max_8192():
    assert max_8192(3, 7) == 7
