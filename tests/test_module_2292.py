"""Tests for test module 2292 — covers src modules [9165, 9166, 9167, 9168]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9165 import modulo_9165
from module_9166 import power_9166
from module_9167 import min_9167
from module_9168 import max_9168

def test_modulo_9165():
    assert modulo_9165(10, 3) == 1

def test_power_9166():
    assert power_9166(2, 8) == 256

def test_min_9167():
    assert min_9167(3, 7) == 3

def test_max_9168():
    assert max_9168(3, 7) == 7
