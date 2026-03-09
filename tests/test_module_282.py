"""Tests for test module 282 — covers src modules [1125, 1126, 1127, 1128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1125 import modulo_1125
from module_1126 import power_1126
from module_1127 import min_1127
from module_1128 import max_1128

def test_modulo_1125():
    assert modulo_1125(10, 3) == 1

def test_power_1126():
    assert power_1126(2, 8) == 256

def test_min_1127():
    assert min_1127(3, 7) == 3

def test_max_1128():
    assert max_1128(3, 7) == 7
