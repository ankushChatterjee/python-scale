"""Tests for test module 1200 — covers src modules [4797, 4798, 4799, 4800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4797 import modulo_4797
from module_4798 import power_4798
from module_4799 import min_4799
from module_4800 import max_4800

def test_modulo_4797():
    assert modulo_4797(10, 3) == 1

def test_power_4798():
    assert power_4798(2, 8) == 256

def test_min_4799():
    assert min_4799(3, 7) == 3

def test_max_4800():
    assert max_4800(3, 7) == 7
