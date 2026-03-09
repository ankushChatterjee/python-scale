"""Tests for test module 1718 — covers src modules [6869, 6870, 6871, 6872]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6869 import modulo_6869
from module_6870 import power_6870
from module_6871 import min_6871
from module_6872 import max_6872

def test_modulo_6869():
    assert modulo_6869(10, 3) == 1

def test_power_6870():
    assert power_6870(2, 8) == 256

def test_min_6871():
    assert min_6871(3, 7) == 3

def test_max_6872():
    assert max_6872(3, 7) == 7
