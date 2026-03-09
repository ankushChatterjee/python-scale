"""Tests for test module 2492 — covers src modules [9965, 9966, 9967, 9968]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9965 import modulo_9965
from module_9966 import power_9966
from module_9967 import min_9967
from module_9968 import max_9968

def test_modulo_9965():
    assert modulo_9965(10, 3) == 1

def test_power_9966():
    assert power_9966(2, 8) == 256

def test_min_9967():
    assert min_9967(3, 7) == 3

def test_max_9968():
    assert max_9968(3, 7) == 7
