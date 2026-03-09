"""Tests for test module 1094 — covers src modules [4373, 4374, 4375, 4376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4373 import modulo_4373
from module_4374 import power_4374
from module_4375 import min_4375
from module_4376 import max_4376

def test_modulo_4373():
    assert modulo_4373(10, 3) == 1

def test_power_4374():
    assert power_4374(2, 8) == 256

def test_min_4375():
    assert min_4375(3, 7) == 3

def test_max_4376():
    assert max_4376(3, 7) == 7
