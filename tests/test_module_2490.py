"""Tests for test module 2490 — covers src modules [9957, 9958, 9959, 9960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9957 import modulo_9957
from module_9958 import power_9958
from module_9959 import min_9959
from module_9960 import max_9960

def test_modulo_9957():
    assert modulo_9957(10, 3) == 1

def test_power_9958():
    assert power_9958(2, 8) == 256

def test_min_9959():
    assert min_9959(3, 7) == 3

def test_max_9960():
    assert max_9960(3, 7) == 7
