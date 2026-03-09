"""Tests for test module 1802 — covers src modules [7205, 7206, 7207, 7208]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7205 import modulo_7205
from module_7206 import power_7206
from module_7207 import min_7207
from module_7208 import max_7208

def test_modulo_7205():
    assert modulo_7205(10, 3) == 1

def test_power_7206():
    assert power_7206(2, 8) == 256

def test_min_7207():
    assert min_7207(3, 7) == 3

def test_max_7208():
    assert max_7208(3, 7) == 7
