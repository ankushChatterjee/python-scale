"""Tests for test module 906 — covers src modules [3621, 3622, 3623, 3624]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3621 import modulo_3621
from module_3622 import power_3622
from module_3623 import min_3623
from module_3624 import max_3624

def test_modulo_3621():
    assert modulo_3621(10, 3) == 1

def test_power_3622():
    assert power_3622(2, 8) == 256

def test_min_3623():
    assert min_3623(3, 7) == 3

def test_max_3624():
    assert max_3624(3, 7) == 7
