"""Tests for test module 1468 — covers src modules [5869, 5870, 5871, 5872]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5869 import modulo_5869
from module_5870 import power_5870
from module_5871 import min_5871
from module_5872 import max_5872

def test_modulo_5869():
    assert modulo_5869(10, 3) == 1

def test_power_5870():
    assert power_5870(2, 8) == 256

def test_min_5871():
    assert min_5871(3, 7) == 3

def test_max_5872():
    assert max_5872(3, 7) == 7
