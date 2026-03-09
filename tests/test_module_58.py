"""Tests for test module 58 — covers src modules [229, 230, 231, 232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_229 import modulo_229
from module_230 import power_230
from module_231 import min_231
from module_232 import max_232

def test_modulo_229():
    assert modulo_229(10, 3) == 1

def test_power_230():
    assert power_230(2, 8) == 256

def test_min_231():
    assert min_231(3, 7) == 3

def test_max_232():
    assert max_232(3, 7) == 7
