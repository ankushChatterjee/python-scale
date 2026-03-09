"""Tests for test module 468 — covers src modules [1869, 1870, 1871, 1872]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1869 import modulo_1869
from module_1870 import power_1870
from module_1871 import min_1871
from module_1872 import max_1872

def test_modulo_1869():
    assert modulo_1869(10, 3) == 1

def test_power_1870():
    assert power_1870(2, 8) == 256

def test_min_1871():
    assert min_1871(3, 7) == 3

def test_max_1872():
    assert max_1872(3, 7) == 7
