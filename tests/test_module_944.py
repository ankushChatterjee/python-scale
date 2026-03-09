"""Tests for test module 944 — covers src modules [3773, 3774, 3775, 3776]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3773 import modulo_3773
from module_3774 import power_3774
from module_3775 import min_3775
from module_3776 import max_3776

def test_modulo_3773():
    assert modulo_3773(10, 3) == 1

def test_power_3774():
    assert power_3774(2, 8) == 256

def test_min_3775():
    assert min_3775(3, 7) == 3

def test_max_3776():
    assert max_3776(3, 7) == 7
