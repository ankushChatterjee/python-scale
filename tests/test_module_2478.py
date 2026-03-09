"""Tests for test module 2478 — covers src modules [9909, 9910, 9911, 9912]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9909 import modulo_9909
from module_9910 import power_9910
from module_9911 import min_9911
from module_9912 import max_9912

def test_modulo_9909():
    assert modulo_9909(10, 3) == 1

def test_power_9910():
    assert power_9910(2, 8) == 256

def test_min_9911():
    assert min_9911(3, 7) == 3

def test_max_9912():
    assert max_9912(3, 7) == 7
