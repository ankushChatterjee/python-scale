"""Tests for test module 422 — covers src modules [1685, 1686, 1687, 1688]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1685 import modulo_1685
from module_1686 import power_1686
from module_1687 import min_1687
from module_1688 import max_1688

def test_modulo_1685():
    assert modulo_1685(10, 3) == 1

def test_power_1686():
    assert power_1686(2, 8) == 256

def test_min_1687():
    assert min_1687(3, 7) == 3

def test_max_1688():
    assert max_1688(3, 7) == 7
