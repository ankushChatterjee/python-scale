"""Tests for test module 718 — covers src modules [2869, 2870, 2871, 2872]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2869 import modulo_2869
from module_2870 import power_2870
from module_2871 import min_2871
from module_2872 import max_2872

def test_modulo_2869():
    assert modulo_2869(10, 3) == 1

def test_power_2870():
    assert power_2870(2, 8) == 256

def test_min_2871():
    assert min_2871(3, 7) == 3

def test_max_2872():
    assert max_2872(3, 7) == 7
