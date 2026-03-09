"""Tests for test module 2398 — covers src modules [9589, 9590, 9591, 9592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9589 import modulo_9589
from module_9590 import power_9590
from module_9591 import min_9591
from module_9592 import max_9592

def test_modulo_9589():
    assert modulo_9589(10, 3) == 1

def test_power_9590():
    assert power_9590(2, 8) == 256

def test_min_9591():
    assert min_9591(3, 7) == 3

def test_max_9592():
    assert max_9592(3, 7) == 7
