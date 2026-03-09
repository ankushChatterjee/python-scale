"""Tests for test module 2422 — covers src modules [9685, 9686, 9687, 9688]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9685 import modulo_9685
from module_9686 import power_9686
from module_9687 import min_9687
from module_9688 import max_9688

def test_modulo_9685():
    assert modulo_9685(10, 3) == 1

def test_power_9686():
    assert power_9686(2, 8) == 256

def test_min_9687():
    assert min_9687(3, 7) == 3

def test_max_9688():
    assert max_9688(3, 7) == 7
