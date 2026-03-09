"""Tests for test module 1124 — covers src modules [4493, 4494, 4495, 4496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4493 import modulo_4493
from module_4494 import power_4494
from module_4495 import min_4495
from module_4496 import max_4496

def test_modulo_4493():
    assert modulo_4493(10, 3) == 1

def test_power_4494():
    assert power_4494(2, 8) == 256

def test_min_4495():
    assert min_4495(3, 7) == 3

def test_max_4496():
    assert max_4496(3, 7) == 7
