"""Tests for test module 52 — covers src modules [205, 206, 207, 208]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_205 import modulo_205
from module_206 import power_206
from module_207 import min_207
from module_208 import max_208

def test_modulo_205():
    assert modulo_205(10, 3) == 1

def test_power_206():
    assert power_206(2, 8) == 256

def test_min_207():
    assert min_207(3, 7) == 3

def test_max_208():
    assert max_208(3, 7) == 7
