"""Tests for test module 1302 — covers src modules [5205, 5206, 5207, 5208]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5205 import modulo_5205
from module_5206 import power_5206
from module_5207 import min_5207
from module_5208 import max_5208

def test_modulo_5205():
    assert modulo_5205(10, 3) == 1

def test_power_5206():
    assert power_5206(2, 8) == 256

def test_min_5207():
    assert min_5207(3, 7) == 3

def test_max_5208():
    assert max_5208(3, 7) == 7
