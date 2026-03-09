"""Tests for test module 672 — covers src modules [2685, 2686, 2687, 2688]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2685 import modulo_2685
from module_2686 import power_2686
from module_2687 import min_2687
from module_2688 import max_2688

def test_modulo_2685():
    assert modulo_2685(10, 3) == 1

def test_power_2686():
    assert power_2686(2, 8) == 256

def test_min_2687():
    assert min_2687(3, 7) == 3

def test_max_2688():
    assert max_2688(3, 7) == 7
