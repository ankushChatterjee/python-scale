"""Tests for test module 562 — covers src modules [2245, 2246, 2247, 2248]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2245 import modulo_2245
from module_2246 import power_2246
from module_2247 import min_2247
from module_2248 import max_2248

def test_modulo_2245():
    assert modulo_2245(10, 3) == 1

def test_power_2246():
    assert power_2246(2, 8) == 256

def test_min_2247():
    assert min_2247(3, 7) == 3

def test_max_2248():
    assert max_2248(3, 7) == 7
