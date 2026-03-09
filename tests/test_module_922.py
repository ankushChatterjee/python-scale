"""Tests for test module 922 — covers src modules [3685, 3686, 3687, 3688]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3685 import modulo_3685
from module_3686 import power_3686
from module_3687 import min_3687
from module_3688 import max_3688

def test_modulo_3685():
    assert modulo_3685(10, 3) == 1

def test_power_3686():
    assert power_3686(2, 8) == 256

def test_min_3687():
    assert min_3687(3, 7) == 3

def test_max_3688():
    assert max_3688(3, 7) == 7
