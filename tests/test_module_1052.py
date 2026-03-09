"""Tests for test module 1052 — covers src modules [4205, 4206, 4207, 4208]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4205 import modulo_4205
from module_4206 import power_4206
from module_4207 import min_4207
from module_4208 import max_4208

def test_modulo_4205():
    assert modulo_4205(10, 3) == 1

def test_power_4206():
    assert power_4206(2, 8) == 256

def test_min_4207():
    assert min_4207(3, 7) == 3

def test_max_4208():
    assert max_4208(3, 7) == 7
