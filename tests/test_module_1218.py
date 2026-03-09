"""Tests for test module 1218 — covers src modules [4869, 4870, 4871, 4872]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4869 import modulo_4869
from module_4870 import power_4870
from module_4871 import min_4871
from module_4872 import max_4872

def test_modulo_4869():
    assert modulo_4869(10, 3) == 1

def test_power_4870():
    assert power_4870(2, 8) == 256

def test_min_4871():
    assert min_4871(3, 7) == 3

def test_max_4872():
    assert max_4872(3, 7) == 7
