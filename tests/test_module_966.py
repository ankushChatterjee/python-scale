"""Tests for test module 966 — covers src modules [3861, 3862, 3863, 3864]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3861 import modulo_3861
from module_3862 import power_3862
from module_3863 import min_3863
from module_3864 import max_3864

def test_modulo_3861():
    assert modulo_3861(10, 3) == 1

def test_power_3862():
    assert power_3862(2, 8) == 256

def test_min_3863():
    assert min_3863(3, 7) == 3

def test_max_3864():
    assert max_3864(3, 7) == 7
