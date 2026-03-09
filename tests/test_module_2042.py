"""Tests for test module 2042 — covers src modules [8165, 8166, 8167, 8168]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8165 import modulo_8165
from module_8166 import power_8166
from module_8167 import min_8167
from module_8168 import max_8168

def test_modulo_8165():
    assert modulo_8165(10, 3) == 1

def test_power_8166():
    assert power_8166(2, 8) == 256

def test_min_8167():
    assert min_8167(3, 7) == 3

def test_max_8168():
    assert max_8168(3, 7) == 7
