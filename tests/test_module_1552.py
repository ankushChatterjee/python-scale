"""Tests for test module 1552 — covers src modules [6205, 6206, 6207, 6208]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6205 import modulo_6205
from module_6206 import power_6206
from module_6207 import min_6207
from module_6208 import max_6208

def test_modulo_6205():
    assert modulo_6205(10, 3) == 1

def test_power_6206():
    assert power_6206(2, 8) == 256

def test_min_6207():
    assert min_6207(3, 7) == 3

def test_max_6208():
    assert max_6208(3, 7) == 7
