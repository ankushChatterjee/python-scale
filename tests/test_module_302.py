"""Tests for test module 302 — covers src modules [1205, 1206, 1207, 1208]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1205 import modulo_1205
from module_1206 import power_1206
from module_1207 import min_1207
from module_1208 import max_1208

def test_modulo_1205():
    assert modulo_1205(10, 3) == 1

def test_power_1206():
    assert power_1206(2, 8) == 256

def test_min_1207():
    assert min_1207(3, 7) == 3

def test_max_1208():
    assert max_1208(3, 7) == 7
