"""Tests for test module 218 — covers src modules [869, 870, 871, 872]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_869 import modulo_869
from module_870 import power_870
from module_871 import min_871
from module_872 import max_872

def test_modulo_869():
    assert modulo_869(10, 3) == 1

def test_power_870():
    assert power_870(2, 8) == 256

def test_min_871():
    assert min_871(3, 7) == 3

def test_max_872():
    assert max_872(3, 7) == 7
