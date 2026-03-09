"""Tests for test module 968 — covers src modules [3869, 3870, 3871, 3872]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3869 import modulo_3869
from module_3870 import power_3870
from module_3871 import min_3871
from module_3872 import max_3872

def test_modulo_3869():
    assert modulo_3869(10, 3) == 1

def test_power_3870():
    assert power_3870(2, 8) == 256

def test_min_3871():
    assert min_3871(3, 7) == 3

def test_max_3872():
    assert max_3872(3, 7) == 7
