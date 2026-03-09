"""Tests for test module 1062 — covers src modules [4245, 4246, 4247, 4248]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4245 import modulo_4245
from module_4246 import power_4246
from module_4247 import min_4247
from module_4248 import max_4248

def test_modulo_4245():
    assert modulo_4245(10, 3) == 1

def test_power_4246():
    assert power_4246(2, 8) == 256

def test_min_4247():
    assert min_4247(3, 7) == 3

def test_max_4248():
    assert max_4248(3, 7) == 7
