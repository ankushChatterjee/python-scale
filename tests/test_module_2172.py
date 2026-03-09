"""Tests for test module 2172 — covers src modules [8685, 8686, 8687, 8688]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8685 import modulo_8685
from module_8686 import power_8686
from module_8687 import min_8687
from module_8688 import max_8688

def test_modulo_8685():
    assert modulo_8685(10, 3) == 1

def test_power_8686():
    assert power_8686(2, 8) == 256

def test_min_8687():
    assert min_8687(3, 7) == 3

def test_max_8688():
    assert max_8688(3, 7) == 7
