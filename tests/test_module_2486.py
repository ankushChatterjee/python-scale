"""Tests for test module 2486 — covers src modules [9941, 9942, 9943, 9944]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9941 import modulo_9941
from module_9942 import power_9942
from module_9943 import min_9943
from module_9944 import max_9944

def test_modulo_9941():
    assert modulo_9941(10, 3) == 1

def test_power_9942():
    assert power_9942(2, 8) == 256

def test_min_9943():
    assert min_9943(3, 7) == 3

def test_max_9944():
    assert max_9944(3, 7) == 7
