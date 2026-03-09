"""Tests for test module 2406 — covers src modules [9621, 9622, 9623, 9624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9621 import modulo_9621
from module_9622 import power_9622
from module_9623 import min_9623
from module_9624 import max_9624

def test_modulo_9621():
    assert modulo_9621(10, 3) == 1

def test_power_9622():
    assert power_9622(2, 8) == 256

def test_min_9623():
    assert min_9623(3, 7) == 3

def test_max_9624():
    assert max_9624(3, 7) == 7
