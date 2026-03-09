"""Tests for test module 172 — covers src modules [685, 686, 687, 688]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_685 import modulo_685
from module_686 import power_686
from module_687 import min_687
from module_688 import max_688

def test_modulo_685():
    assert modulo_685(10, 3) == 1

def test_power_686():
    assert power_686(2, 8) == 256

def test_min_687():
    assert min_687(3, 7) == 3

def test_max_688():
    assert max_688(3, 7) == 7
