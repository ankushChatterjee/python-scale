"""Tests for test module 1808 — covers src modules [7229, 7230, 7231, 7232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7229 import modulo_7229
from module_7230 import power_7230
from module_7231 import min_7231
from module_7232 import max_7232

def test_modulo_7229():
    assert modulo_7229(10, 3) == 1

def test_power_7230():
    assert power_7230(2, 8) == 256

def test_min_7231():
    assert min_7231(3, 7) == 3

def test_max_7232():
    assert max_7232(3, 7) == 7
