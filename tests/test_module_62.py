"""Tests for test module 62 — covers src modules [245, 246, 247, 248]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_245 import modulo_245
from module_246 import power_246
from module_247 import min_247
from module_248 import max_248

def test_modulo_245():
    assert modulo_245(10, 3) == 1

def test_power_246():
    assert power_246(2, 8) == 256

def test_min_247():
    assert min_247(3, 7) == 3

def test_max_248():
    assert max_248(3, 7) == 7
