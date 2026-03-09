"""Tests for test module 2374 — covers src modules [9493, 9494, 9495, 9496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9493 import modulo_9493
from module_9494 import power_9494
from module_9495 import min_9495
from module_9496 import max_9496

def test_modulo_9493():
    assert modulo_9493(10, 3) == 1

def test_power_9494():
    assert power_9494(2, 8) == 256

def test_min_9495():
    assert min_9495(3, 7) == 3

def test_max_9496():
    assert max_9496(3, 7) == 7
