"""Tests for test module 1812 — covers src modules [7245, 7246, 7247, 7248]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7245 import modulo_7245
from module_7246 import power_7246
from module_7247 import min_7247
from module_7248 import max_7248

def test_modulo_7245():
    assert modulo_7245(10, 3) == 1

def test_power_7246():
    assert power_7246(2, 8) == 256

def test_min_7247():
    assert min_7247(3, 7) == 3

def test_max_7248():
    assert max_7248(3, 7) == 7
