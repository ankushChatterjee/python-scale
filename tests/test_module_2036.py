"""Tests for test module 2036 — covers src modules [8141, 8142, 8143, 8144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8141 import modulo_8141
from module_8142 import power_8142
from module_8143 import min_8143
from module_8144 import max_8144

def test_modulo_8141():
    assert modulo_8141(10, 3) == 1

def test_power_8142():
    assert power_8142(2, 8) == 256

def test_min_8143():
    assert min_8143(3, 7) == 3

def test_max_8144():
    assert max_8144(3, 7) == 7
