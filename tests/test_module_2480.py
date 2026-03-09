"""Tests for test module 2480 — covers src modules [9917, 9918, 9919, 9920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9917 import modulo_9917
from module_9918 import power_9918
from module_9919 import min_9919
from module_9920 import max_9920

def test_modulo_9917():
    assert modulo_9917(10, 3) == 1

def test_power_9918():
    assert power_9918(2, 8) == 256

def test_min_9919():
    assert min_9919(3, 7) == 3

def test_max_9920():
    assert max_9920(3, 7) == 7
