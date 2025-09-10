import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from calculator12 import add, subtract, multiply, divide

# dummy2344
def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 0) is None
    
def test_divide2():
    assert divide(8, 4) == 2
    assert divide(5, 0) is None
