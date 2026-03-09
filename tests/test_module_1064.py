"""Tests for test module 1064 — covers src modules [4253, 4254, 4255, 4256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4253 import modulo_4253
from module_4254 import power_4254
from module_4255 import min_4255
from module_4256 import max_4256

def test_modulo_4253():
    assert modulo_4253(10, 3) == 1

def test_power_4254():
    assert power_4254(2, 8) == 256

def test_min_4255():
    assert min_4255(3, 7) == 3

def test_max_4256():
    assert max_4256(3, 7) == 7
