"""Tests for test module 124 — covers src modules [493, 494, 495, 496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_493 import modulo_493
from module_494 import power_494
from module_495 import min_495
from module_496 import max_496

def test_modulo_493():
    assert modulo_493(10, 3) == 1

def test_power_494():
    assert power_494(2, 8) == 256

def test_min_495():
    assert min_495(3, 7) == 3

def test_max_496():
    assert max_496(3, 7) == 7
