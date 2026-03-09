"""Tests for test module 1084 — covers src modules [4333, 4334, 4335, 4336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4333 import modulo_4333
from module_4334 import power_4334
from module_4335 import min_4335
from module_4336 import max_4336

def test_modulo_4333():
    assert modulo_4333(10, 3) == 1

def test_power_4334():
    assert power_4334(2, 8) == 256

def test_min_4335():
    assert min_4335(3, 7) == 3

def test_max_4336():
    assert max_4336(3, 7) == 7
