"""Tests for test module 2394 — covers src modules [9573, 9574, 9575, 9576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9573 import modulo_9573
from module_9574 import power_9574
from module_9575 import min_9575
from module_9576 import max_9576

def test_modulo_9573():
    assert modulo_9573(10, 3) == 1

def test_power_9574():
    assert power_9574(2, 8) == 256

def test_min_9575():
    assert min_9575(3, 7) == 3

def test_max_9576():
    assert max_9576(3, 7) == 7
