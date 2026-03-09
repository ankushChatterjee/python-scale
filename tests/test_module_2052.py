"""Tests for test module 2052 — covers src modules [8205, 8206, 8207, 8208]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8205 import modulo_8205
from module_8206 import power_8206
from module_8207 import min_8207
from module_8208 import max_8208

def test_modulo_8205():
    assert modulo_8205(10, 3) == 1

def test_power_8206():
    assert power_8206(2, 8) == 256

def test_min_8207():
    assert min_8207(3, 7) == 3

def test_max_8208():
    assert max_8208(3, 7) == 7
