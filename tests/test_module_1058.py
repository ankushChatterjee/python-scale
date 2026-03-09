"""Tests for test module 1058 — covers src modules [4229, 4230, 4231, 4232]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4229 import modulo_4229
from module_4230 import power_4230
from module_4231 import min_4231
from module_4232 import max_4232

def test_modulo_4229():
    assert modulo_4229(10, 3) == 1

def test_power_4230():
    assert power_4230(2, 8) == 256

def test_min_4231():
    assert min_4231(3, 7) == 3

def test_max_4232():
    assert max_4232(3, 7) == 7
