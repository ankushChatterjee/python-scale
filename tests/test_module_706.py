"""Tests for test module 706 — covers src modules [2821, 2822, 2823, 2824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2821 import modulo_2821
from module_2822 import power_2822
from module_2823 import min_2823
from module_2824 import max_2824

def test_modulo_2821():
    assert modulo_2821(10, 3) == 1

def test_power_2822():
    assert power_2822(2, 8) == 256

def test_min_2823():
    assert min_2823(3, 7) == 3

def test_max_2824():
    assert max_2824(3, 7) == 7
