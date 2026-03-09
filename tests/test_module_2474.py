"""Tests for test module 2474 — covers src modules [9893, 9894, 9895, 9896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9893 import modulo_9893
from module_9894 import power_9894
from module_9895 import min_9895
from module_9896 import max_9896

def test_modulo_9893():
    assert modulo_9893(10, 3) == 1

def test_power_9894():
    assert power_9894(2, 8) == 256

def test_min_9895():
    assert min_9895(3, 7) == 3

def test_max_9896():
    assert max_9896(3, 7) == 7
