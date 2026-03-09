"""Tests for test module 312 — covers src modules [1245, 1246, 1247, 1248]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1245 import modulo_1245
from module_1246 import power_1246
from module_1247 import min_1247
from module_1248 import max_1248

def test_modulo_1245():
    assert modulo_1245(10, 3) == 1

def test_power_1246():
    assert power_1246(2, 8) == 256

def test_min_1247():
    assert min_1247(3, 7) == 3

def test_max_1248():
    assert max_1248(3, 7) == 7
