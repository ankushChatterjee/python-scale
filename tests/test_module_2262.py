"""Tests for test module 2262 — covers src modules [9045, 9046, 9047, 9048]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9045 import modulo_9045
from module_9046 import power_9046
from module_9047 import min_9047
from module_9048 import max_9048

def test_modulo_9045():
    assert modulo_9045(10, 3) == 1

def test_power_9046():
    assert power_9046(2, 8) == 256

def test_min_9047():
    assert min_9047(3, 7) == 3

def test_max_9048():
    assert max_9048(3, 7) == 7
