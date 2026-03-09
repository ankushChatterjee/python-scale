"""Tests for test module 2360 — covers src modules [9437, 9438, 9439, 9440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9437 import modulo_9437
from module_9438 import power_9438
from module_9439 import min_9439
from module_9440 import max_9440

def test_modulo_9437():
    assert modulo_9437(10, 3) == 1

def test_power_9438():
    assert power_9438(2, 8) == 256

def test_min_9439():
    assert min_9439(3, 7) == 3

def test_max_9440():
    assert max_9440(3, 7) == 7
