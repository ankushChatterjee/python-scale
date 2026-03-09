"""Tests for test module 506 — covers src modules [2021, 2022, 2023, 2024]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2021 import modulo_2021
from module_2022 import power_2022
from module_2023 import min_2023
from module_2024 import max_2024

def test_modulo_2021():
    assert modulo_2021(10, 3) == 1

def test_power_2022():
    assert power_2022(2, 8) == 256

def test_min_2023():
    assert min_2023(3, 7) == 3

def test_max_2024():
    assert max_2024(3, 7) == 7
