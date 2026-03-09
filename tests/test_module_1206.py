"""Tests for test module 1206 — covers src modules [4821, 4822, 4823, 4824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4821 import modulo_4821
from module_4822 import power_4822
from module_4823 import min_4823
from module_4824 import max_4824

def test_modulo_4821():
    assert modulo_4821(10, 3) == 1

def test_power_4822():
    assert power_4822(2, 8) == 256

def test_min_4823():
    assert min_4823(3, 7) == 3

def test_max_4824():
    assert max_4824(3, 7) == 7
