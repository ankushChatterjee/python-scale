"""Tests for test module 1126 — covers src modules [4501, 4502, 4503, 4504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4501 import modulo_4501
from module_4502 import power_4502
from module_4503 import min_4503
from module_4504 import max_4504

def test_modulo_4501():
    assert modulo_4501(10, 3) == 1

def test_power_4502():
    assert power_4502(2, 8) == 256

def test_min_4503():
    assert min_4503(3, 7) == 3

def test_max_4504():
    assert max_4504(3, 7) == 7
