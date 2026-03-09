"""Tests for test module 2420 — covers src modules [9677, 9678, 9679, 9680]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9677 import modulo_9677
from module_9678 import power_9678
from module_9679 import min_9679
from module_9680 import max_9680

def test_modulo_9677():
    assert modulo_9677(10, 3) == 1

def test_power_9678():
    assert power_9678(2, 8) == 256

def test_min_9679():
    assert min_9679(3, 7) == 3

def test_max_9680():
    assert max_9680(3, 7) == 7
