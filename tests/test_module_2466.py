"""Tests for test module 2466 — covers src modules [9861, 9862, 9863, 9864]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9861 import modulo_9861
from module_9862 import power_9862
from module_9863 import min_9863
from module_9864 import max_9864

def test_modulo_9861():
    assert modulo_9861(10, 3) == 1

def test_power_9862():
    assert power_9862(2, 8) == 256

def test_min_9863():
    assert min_9863(3, 7) == 3

def test_max_9864():
    assert max_9864(3, 7) == 7
