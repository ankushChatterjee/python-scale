"""Tests for test module 1240 — covers src modules [4957, 4958, 4959, 4960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4957 import modulo_4957
from module_4958 import power_4958
from module_4959 import min_4959
from module_4960 import max_4960

def test_modulo_4957():
    assert modulo_4957(10, 3) == 1

def test_power_4958():
    assert power_4958(2, 8) == 256

def test_min_4959():
    assert min_4959(3, 7) == 3

def test_max_4960():
    assert max_4960(3, 7) == 7
