"""Tests for test module 1968 — covers src modules [7869, 7870, 7871, 7872]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7869 import modulo_7869
from module_7870 import power_7870
from module_7871 import min_7871
from module_7872 import max_7872

def test_modulo_7869():
    assert modulo_7869(10, 3) == 1

def test_power_7870():
    assert power_7870(2, 8) == 256

def test_min_7871():
    assert min_7871(3, 7) == 3

def test_max_7872():
    assert max_7872(3, 7) == 7
