"""Tests for test module 1298 — covers src modules [5189, 5190, 5191, 5192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5189 import modulo_5189
from module_5190 import power_5190
from module_5191 import min_5191
from module_5192 import max_5192

def test_modulo_5189():
    assert modulo_5189(10, 3) == 1

def test_power_5190():
    assert power_5190(2, 8) == 256

def test_min_5191():
    assert min_5191(3, 7) == 3

def test_max_5192():
    assert max_5192(3, 7) == 7
