"""Tests for test module 402 — covers src modules [1605, 1606, 1607, 1608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1605 import modulo_1605
from module_1606 import power_1606
from module_1607 import min_1607
from module_1608 import max_1608

def test_modulo_1605():
    assert modulo_1605(10, 3) == 1

def test_power_1606():
    assert power_1606(2, 8) == 256

def test_min_1607():
    assert min_1607(3, 7) == 3

def test_max_1608():
    assert max_1608(3, 7) == 7
