"""Tests for test module 374 — covers src modules [1493, 1494, 1495, 1496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1493 import modulo_1493
from module_1494 import power_1494
from module_1495 import min_1495
from module_1496 import max_1496

def test_modulo_1493():
    assert modulo_1493(10, 3) == 1

def test_power_1494():
    assert power_1494(2, 8) == 256

def test_min_1495():
    assert min_1495(3, 7) == 3

def test_max_1496():
    assert max_1496(3, 7) == 7
