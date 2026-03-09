"""Tests for test module 1422 — covers src modules [5685, 5686, 5687, 5688]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5685 import modulo_5685
from module_5686 import power_5686
from module_5687 import min_5687
from module_5688 import max_5688

def test_modulo_5685():
    assert modulo_5685(10, 3) == 1

def test_power_5686():
    assert power_5686(2, 8) == 256

def test_min_5687():
    assert min_5687(3, 7) == 3

def test_max_5688():
    assert max_5688(3, 7) == 7
