"""Tests for test module 2298 — covers src modules [9189, 9190, 9191, 9192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9189 import modulo_9189
from module_9190 import power_9190
from module_9191 import min_9191
from module_9192 import max_9192

def test_modulo_9189():
    assert modulo_9189(10, 3) == 1

def test_power_9190():
    assert power_9190(2, 8) == 256

def test_min_9191():
    assert min_9191(3, 7) == 3

def test_max_9192():
    assert max_9192(3, 7) == 7
