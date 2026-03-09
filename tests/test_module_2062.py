"""Tests for test module 2062 — covers src modules [8245, 8246, 8247, 8248]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8245 import modulo_8245
from module_8246 import power_8246
from module_8247 import min_8247
from module_8248 import max_8248

def test_modulo_8245():
    assert modulo_8245(10, 3) == 1

def test_power_8246():
    assert power_8246(2, 8) == 256

def test_min_8247():
    assert min_8247(3, 7) == 3

def test_max_8248():
    assert max_8248(3, 7) == 7
