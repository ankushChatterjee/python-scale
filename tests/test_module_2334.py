"""Tests for test module 2334 — covers src modules [9333, 9334, 9335, 9336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9333 import modulo_9333
from module_9334 import power_9334
from module_9335 import min_9335
from module_9336 import max_9336

def test_modulo_9333():
    assert modulo_9333(10, 3) == 1

def test_power_9334():
    assert power_9334(2, 8) == 256

def test_min_9335():
    assert min_9335(3, 7) == 3

def test_max_9336():
    assert max_9336(3, 7) == 7
