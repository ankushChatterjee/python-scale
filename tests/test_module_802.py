"""Tests for test module 802 — covers src modules [3205, 3206, 3207, 3208]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3205 import modulo_3205
from module_3206 import power_3206
from module_3207 import min_3207
from module_3208 import max_3208

def test_modulo_3205():
    assert modulo_3205(10, 3) == 1

def test_power_3206():
    assert power_3206(2, 8) == 256

def test_min_3207():
    assert min_3207(3, 7) == 3

def test_max_3208():
    assert max_3208(3, 7) == 7
