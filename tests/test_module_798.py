"""Tests for test module 798 — covers src modules [3189, 3190, 3191, 3192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3189 import modulo_3189
from module_3190 import power_3190
from module_3191 import min_3191
from module_3192 import max_3192

def test_modulo_3189():
    assert modulo_3189(10, 3) == 1

def test_power_3190():
    assert power_3190(2, 8) == 256

def test_min_3191():
    assert min_3191(3, 7) == 3

def test_max_3192():
    assert max_3192(3, 7) == 7
