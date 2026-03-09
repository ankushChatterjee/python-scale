"""Tests for test module 2498 — covers src modules [9989, 9990, 9991, 9992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9989 import modulo_9989
from module_9990 import power_9990
from module_9991 import min_9991
from module_9992 import max_9992

def test_modulo_9989():
    assert modulo_9989(10, 3) == 1

def test_power_9990():
    assert power_9990(2, 8) == 256

def test_min_9991():
    assert min_9991(3, 7) == 3

def test_max_9992():
    assert max_9992(3, 7) == 7
