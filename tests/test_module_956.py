"""Tests for test module 956 — covers src modules [3821, 3822, 3823, 3824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3821 import modulo_3821
from module_3822 import power_3822
from module_3823 import min_3823
from module_3824 import max_3824

def test_modulo_3821():
    assert modulo_3821(10, 3) == 1

def test_power_3822():
    assert power_3822(2, 8) == 256

def test_min_3823():
    assert min_3823(3, 7) == 3

def test_max_3824():
    assert max_3824(3, 7) == 7
