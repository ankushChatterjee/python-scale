"""Tests for test module 938 — covers src modules [3749, 3750, 3751, 3752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3749 import modulo_3749
from module_3750 import power_3750
from module_3751 import min_3751
from module_3752 import max_3752

def test_modulo_3749():
    assert modulo_3749(10, 3) == 1

def test_power_3750():
    assert power_3750(2, 8) == 256

def test_min_3751():
    assert min_3751(3, 7) == 3

def test_max_3752():
    assert max_3752(3, 7) == 7
