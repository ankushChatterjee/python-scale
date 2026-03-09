"""Tests for test module 1050 — covers src modules [4197, 4198, 4199, 4200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4197 import modulo_4197
from module_4198 import power_4198
from module_4199 import min_4199
from module_4200 import max_4200

def test_modulo_4197():
    assert modulo_4197(10, 3) == 1

def test_power_4198():
    assert power_4198(2, 8) == 256

def test_min_4199():
    assert min_4199(3, 7) == 3

def test_max_4200():
    assert max_4200(3, 7) == 7
