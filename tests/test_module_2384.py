"""Tests for test module 2384 — covers src modules [9533, 9534, 9535, 9536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9533 import modulo_9533
from module_9534 import power_9534
from module_9535 import min_9535
from module_9536 import max_9536

def test_modulo_9533():
    assert modulo_9533(10, 3) == 1

def test_power_9534():
    assert power_9534(2, 8) == 256

def test_min_9535():
    assert min_9535(3, 7) == 3

def test_max_9536():
    assert max_9536(3, 7) == 7
