"""Tests for test module 1562 — covers src modules [6245, 6246, 6247, 6248]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6245 import modulo_6245
from module_6246 import power_6246
from module_6247 import min_6247
from module_6248 import max_6248

def test_modulo_6245():
    assert modulo_6245(10, 3) == 1

def test_power_6246():
    assert power_6246(2, 8) == 256

def test_min_6247():
    assert min_6247(3, 7) == 3

def test_max_6248():
    assert max_6248(3, 7) == 7
