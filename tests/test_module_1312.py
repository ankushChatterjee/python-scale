"""Tests for test module 1312 — covers src modules [5245, 5246, 5247, 5248]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5245 import modulo_5245
from module_5246 import power_5246
from module_5247 import min_5247
from module_5248 import max_5248

def test_modulo_5245():
    assert modulo_5245(10, 3) == 1

def test_power_5246():
    assert power_5246(2, 8) == 256

def test_min_5247():
    assert min_5247(3, 7) == 3

def test_max_5248():
    assert max_5248(3, 7) == 7
